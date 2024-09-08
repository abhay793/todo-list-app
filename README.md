# To-Do List Application

## Overview

This repository contains a simple To-Do List application with two main components:
1. **Backend API**: A RESTful API built using Flask and SQLite for managing to-do items.
2. **Frontend Web Application**: A user interface built with HTML, CSS, and JavaScript for interacting with the API.

## Project Structure


## Files and Directories

### Backend (API)

- **`api/app.py`**:
  - This file contains the Flask application that provides the RESTful API for managing to-do items.
  - **Code Breakdown**:
    - **Imports**:
      - `Flask`, `request`, `jsonify`, `abort` from `flask`: For creating the web application and handling HTTP requests and responses.
      - `sqlite3`: For interacting with the SQLite database.
    - **Database Initialization (`init_db` function)**:
      - Creates a SQLite database (`todos.db`) and a table (`todos`) if they do not already exist.
    - **API Endpoints**:
      - `GET /todos`: Retrieves a list of all to-do items from the database.
      - `POST /todos`: Adds a new to-do item to the database. Requires `title` and `description` in the request body.
      - `PUT /todos/<id>`: Updates an existing to-do item specified by `id`.
      - `DELETE /todos/<id>`: Deletes a to-do item specified by `id`.
    - **Error Handling**:
      - Handles `404` and `400` errors with appropriate JSON responses.

- **`api/requirements.txt`**:
  - Lists the Python dependencies required for the API.
  - Includes:
    - `Flask`: For building the web application.

### Frontend (Web Application)

- **`web/index.html`**:
  - The main HTML file for the web application.
  - **Code Breakdown**:
    - Contains a form to add new to-do items.
    - Displays the list of existing to-do items with options to mark as completed or delete.

- **`web/styles.css`**:
  - Provides the styling for the web application.
  - **Code Breakdown**:
    - **Global Styles**:
      - Styles the body, container, header, and general layout.
    - **Form Styles**:
      - Styles the input fields and buttons for adding new to-dos.
    - **To-Do List Styles**:
      - Styles the individual to-do items and their actions (completed, delete).
    - **Responsive Design**:
      - Ensures the application looks good on different screen sizes.

- **`web/app.js`**:
  - Contains JavaScript code to interact with the API and manage the user interface.
  - **Code Breakdown**:
    - **Fetch To-Do Items**:
      - Makes a `GET` request to retrieve and display the list of to-do items.
    - **Add New To-Do**:
      - Sends a `POST` request to add a new to-do item.
    - **Update To-Do**:
      - Sends a `PUT` request to mark a to-do item as completed.
    - **Delete To-Do**:
      - Sends a `DELETE` request to remove a to-do item.

## Installation and Setup

### Backend (API)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/todo-list-app.git
   cd todo-list-app/api

### Key Points in the README:

- **Project Structure**: Describes the organization of the files and directories.
- **Files and Directories**: Provides details on what each file and directory contains and its purpose.
- **Installation and Setup**: Instructions for setting up and running both the backend and frontend.
- **Usage**: How to use the API and web application.
- **Contributing**: Encourages collaboration and outlines how to contribute.
- **License**: Specifies the licensing terms.
- **Contact**: Provides contact information for further communication.

Feel free to modify and expand upon this README to better fit the specifics of your project or any additional features you may have implemented.
