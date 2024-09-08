from flask import Flask, request, jsonify, abort, render_template
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Render the HTML page for the To-Do list UI
@app.route('/')
def index():
    return render_template('index.html')

# Get all to-do items
@app.route('/todos', methods=['GET'])
def get_todos():
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    conn.close()

    return jsonify([{'id': row[0], 'title': row[1], 'description': row[2], 'completed': bool(row[3])} for row in todos])

# Add a new to-do item
@app.route('/todos', methods=['POST'])
def add_todo():
    if not request.json or 'title' not in request.json or 'description' not in request.json:
        abort(400, "Title and description are required")

    new_todo = {
        'title': request.json['title'],
        'description': request.json['description'],
        'completed': False
    }

    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (title, description, completed) VALUES (?, ?, ?)",
                   (new_todo['title'], new_todo['description'], new_todo['completed']))
    conn.commit()
    new_todo['id'] = cursor.lastrowid
    conn.close()

    return jsonify(new_todo), 201

# Update a to-do item
@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    if not request.json:
        abort(400, "Invalid request")

    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM todos WHERE id=?", (id,))
    todo = cursor.fetchone()

    if todo is None:
        abort(404, "To-do item not found")

    title = request.json.get('title', todo[1])
    description = request.json.get('description', todo[2])
    completed = request.json.get('completed', todo[3])

    cursor.execute("UPDATE todos SET title=?, description=?, completed=? WHERE id=?",
                   (title, description, completed, id))
    conn.commit()
    conn.close()

    return jsonify({'id': id, 'title': title, 'description': description, 'completed': bool(completed)})

# Delete a to-do item
@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM todos WHERE id=?", (id,))
    todo = cursor.fetchone()

    if todo is None:
        abort(404, "To-do item not found")

    cursor.execute("DELETE FROM todos WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "To-do item deleted successfully"})

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
