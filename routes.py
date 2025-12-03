from app import app
from flask import render_template

todos = [
    {
        "id": 1,
        "title": "title1",
        "description": "description1",
        "created_at": "2025-11-12 06:27:37",
    },
    {
        "id": 2,
        "title": "title2",
        "description": "description2",
        "created_at": "2025-11-12 06:27:37",
    },
    {
        "id": 3,
        "title": "title3",
        "description": "description3",
        "created_at": "2025-11-12 06:27:37",
    }
]

@app.route('/') # www.domain.com
def index():
    todo_count = len(todos)
    return render_template('index.html', count=todo_count)

@app.route('/tasks') # www.domain.com/tasks
def all_tasks():
    return render_template('tasks.html')    

@app.route('/task/<int:task_id>') # www.domain.com/task/1
def task(task_id):
    return f"<h1>Task detail page for task {task_id}</h1>"

# www.domain.com/new-task
@app.route('/new-task')
def new_task():
    return render_template('new_task.html')