from .tasks import update_task

def set_priority(task_id, priority):
    if priority not in ["Low", "Medium", "High"]:
        print("❌ Invalid priority! Use Low, Medium, or High.")
        return
    update_task(task_id, priority=priority)
