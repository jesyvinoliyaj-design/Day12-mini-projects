import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "records.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"students": [], "teachers": [], "subjects": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_teacher(teacher_id, name, subject_specialization):
    data = load_data()
    data["teachers"].append({
        "id": teacher_id,
        "name": name,
        "specialization": subject_specialization
    })
    save_data(data)
