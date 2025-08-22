import json, os, datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "records.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"income": [], "expense": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_income(amount, source):
    data = load_data()
    entry = {
        "amount": amount,
        "source": source,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data["income"].append(entry)
    save_data(data)

def get_total_income():
    data = load_data()
    return sum(item["amount"] for item in data["income"])
