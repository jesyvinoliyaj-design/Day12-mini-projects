from ..students.register import load_data

def list_students():
    data = load_data()
    return data["students"]
