from ..teachers.register import load_data, save_data

def assign_teacher(teacher_id, subject_id):
    data = load_data()
    for teacher in data["teachers"]:
        if teacher["id"] == teacher_id:
            teacher["assigned_subject"] = subject_id
    save_data(data)
