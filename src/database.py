import sqlite3

import pandas as pd

DB_FILE = "data.db"


# Initialize the database and create tables
def initialize_database():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        # Create projects table
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
        """
        )
        # Create tasks table
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            owner TEXT,
            status TEXT,
            due_date TEXT,
            priority TEXT,
            project_id INTEGER,
            depends_on TEXT,
            comments TEXT,
            time_spent REAL,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        )
        """
        )
        conn.commit()


# Get all projects
def get_projects():
    with sqlite3.connect(DB_FILE) as conn:
        return pd.read_sql("SELECT * FROM projects", conn)


# Add a new project
def add_project(name, description):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO projects (name, description) VALUES (?, ?)",
            (name, description),
        )
        conn.commit()


# Update an existing project
def update_project(project_id, name, description):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE projects SET name = ?, description = ? WHERE id = ?",
            (name, description, project_id),
        )
        conn.commit()


# Delete a project and its associated tasks
def delete_project(project_id):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE project_id = ?", (project_id,))
        cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
        conn.commit()


# Get all tasks
def get_tasks():
    with sqlite3.connect(DB_FILE) as conn:
        return pd.read_sql(
            """
        SELECT tasks.*, projects.name AS project_name FROM tasks
        LEFT JOIN projects ON tasks.project_id = projects.id
        """,
            conn,
        )


# Add a new task
def add_task(
    name,
    owner,
    status,
    due_date,
    priority,
    project_id,
    depends_on,
    comments,
    time_spent,
):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
        INSERT INTO tasks (name, owner, status, due_date, priority, project_id, depends_on, comments, time_spent)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                name,
                owner,
                status,
                due_date,
                priority,
                project_id,
                depends_on,
                comments,
                time_spent,
            ),
        )
        conn.commit()


# Update an existing task
def update_task(
    task_id,
    name,
    owner,
    status,
    due_date,
    priority,
    project_id,
    depends_on,
    comments,
    time_spent,
):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
        UPDATE tasks
        SET name = ?, owner = ?, status = ?, due_date = ?, priority = ?, project_id = ?, depends_on = ?, comments = ?, time_spent = ?
        WHERE id = ?
        """,
            (
                name,
                owner,
                status,
                due_date,
                priority,
                project_id,
                depends_on,
                comments,
                time_spent,
                task_id,
            ),
        )
        conn.commit()


# Delete a task
def delete_task(task_id):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        # Get the name of the task to be deleted
        cursor.execute("SELECT name FROM tasks WHERE id = ?", (task_id,))
        task_name = cursor.fetchone()
        if task_name:
            task_name = task_name[0]

            # Clear "Depends On" for tasks depending on the deleted task
            cursor.execute(
                "UPDATE tasks SET depends_on = NULL WHERE depends_on = ?",
                (task_name,),
            )

            # Delete the task
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
