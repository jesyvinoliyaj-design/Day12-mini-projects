MENU = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 200,
    "Salad": 150,
    "Juice": 80
}

def show_menu():
    print("=== Restaurant Menu ===")
    for item, price in MENU.items():
        print(f"{item:10} : ₹{price}")
