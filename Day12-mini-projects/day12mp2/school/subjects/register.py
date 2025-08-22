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

def add_subject(subject_id, name):
    data = load_data()
    data["subjects"].append({"id": subject_id, "name": name})
    save_data(data)
