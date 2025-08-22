from ..subjects.register import load_data

def list_subjects():
    data = load_data()
    return data["subjects"]
