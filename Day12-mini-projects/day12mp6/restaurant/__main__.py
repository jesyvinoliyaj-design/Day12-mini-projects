from .menu import show_menu
from .order import Order
from .bill import generate_bill

def main():
    print("=== Welcome to Restaurant Billing System ===")
    order = Order()

    while True:
        show_menu()
        item = input("\nEnter item name (or 'done' to finish): ").title()
        if item.lower() == "done":
            break
        qty = int(input("Enter quantity: "))
        print(order.add_item(item, qty))

    generate_bill(order)

if __name__ == "__main__":
    main()
