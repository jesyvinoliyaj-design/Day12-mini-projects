from .offers import apply_discount

TAX_RATE = 0.05  # 5% GST

def generate_bill(order):
    subtotal = sum(price for _, _, price in order.items)
    discounted = apply_discount(subtotal)
    tax = discounted * TAX_RATE
    total = discounted + tax

    print("\n=== Bill Summary ===")
    print(f"Order ID: {order.order_id}")
    for item, qty, price in order.items:
        print(f"{item:10} x{qty:<2} = ₹{price}")
    print(f"\nSubtotal    : ₹{subtotal:.2f}")
    print(f"After Offer : ₹{discounted:.2f}")
    print(f"Tax (5%)    : ₹{tax:.2f}")
    print(f"Total Bill  : ₹{total:.2f}")
