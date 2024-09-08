document.getElementById('todo-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;

    const response = await fetch('/todos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, description })
    });

    if (response.ok) {
        getTodos();
        document.getElementById('title').value = '';
        document.getElementById('description').value = '';
    }
});

async function getTodos() {
    const response = await fetch('/todos');
    const todos = await response.json();
    const todoList = document.getElementById('todo-list');
    todoList.innerHTML = '';

    todos.forEach(todo => {
        const todoItem = document.createElement('div');
        todoItem.className = 'todo-item' + (todo.completed ? ' completed' : '');
        todoItem.innerHTML = `
            <div>
                <input type="checkbox" class="checkbox" ${todo.completed ? 'checked' : ''} onclick="toggleComplete(${todo.id})">
                <div class="todo-title">${todo.title}</div>
                <div class="todo-description">${todo.description}</div>
            </div>
            <div class="todo-actions">
                <button class="delete-button" onclick="deleteTodo(${todo.id})">Delete</button>
            </div>
        `;
        todoList.appendChild(todoItem);
    });
}

async function toggleComplete(id) {
    const response = await fetch(`/todos/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ completed: true }) // Send updated completion status
    });

    if (response.ok) {
        getTodos();
    }
}

async function deleteTodo(id) {
    await fetch(`/todos/${id}`, { method: 'DELETE' });
    getTodos();
}

window.onload = getTodos;
