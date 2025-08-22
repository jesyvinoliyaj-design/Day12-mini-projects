import json, os
from datetime import datetime
from tabulate import tabulate

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "tasks.json")

def _load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def _save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(title, due, priority="Medium"):
    tasks = _load_tasks()
    task_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = {
        "id": task_id,
        "title": title,
        "due": due,
        "priority": priority,
        "status": "Pending"
    }
    tasks.append(new_task)
    _save_tasks(tasks)
    print("✅ Task added successfully!")

def update_task(task_id, **kwargs):
    tasks = _load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t.update(kwargs)
            _save_tasks(tasks)
            print("✅ Task updated successfully!")
            return
    print("❌ Task not found!")

def delete_task(task_id):
    tasks = _load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    _save_tasks(new_tasks)
    print("🗑️ Task deleted!")

def list_tasks():
    tasks = _load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    table = [[t["id"], t["title"], t["due"], t["priority"], t["status"]] for t in tasks]
    print(tabulate(table, headers=["ID", "Title", "Due Date", "Priority", "Status"], tablefmt="pretty"))
