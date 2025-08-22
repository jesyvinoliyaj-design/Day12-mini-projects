import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "questions.json")

def load_questions():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_questions(questions):
    with open(DATA_FILE, "w") as f:
        json.dump(questions, f, indent=4)
