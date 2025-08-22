import random
from .menu import MENU

class Order:
    def __init__(self):
        self.order_id = random.randint(1000, 9999)
        self.items = []

    def add_item(self, item, qty):
        if item in MENU:
            self.items.append((item, qty, MENU[item] * qty))
            return f"Added {qty} x {item}"
        return f"{item} not on menu."
