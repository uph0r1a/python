class RetailItem:
    def __init__(self, description="", unit=0, price=0):
        self.__description = description
        self.__unit = unit
        self.__price = price

    def get_description(self):
        return self.__description

    def get_unit(self):
        return self.__unit

    def get_price(self):
        return self.__price


class CashRegister:
    def __init__(self):
        self.__cart = []

    def purchase_item(self, item):
        self.__cart.append(item)

    def get_total(self):
        total = 0
        for item in self.__cart:
            total += item.get_price()
        return total

    def show_items(self):
        if not self.__cart:
            print("No items in cart.")
            return

        print("\nItems in your cart:")
        for item in self.__cart:
            print(f"- {item.get_description()} : ${item.get_price():.2f}")

    def clear(self):
        """Clear the cart"""
        self.__cart.clear()


items = [
    RetailItem("Jacket", 12, 59.95),
    RetailItem("Designer Jeans", 40, 34.95),
    RetailItem("Shirt", 20, 24.95),
]

register = CashRegister()

while True:
    print("\nAvailable items:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item.get_description()} - ${item.get_price():.2f}")

    print("0. Checkout")

    choice = int(input("Select an item to purchase (0 to checkout): "))

    if choice == 0:
        break
    elif 1 <= choice <= len(items):
        register.purchase_item(items[choice - 1])
        print("Item added to cart.")
    else:
        print("Invalid choice.")

print("\n--- CHECKOUT ---")
register.show_items()
print(f"\nTotal: ${register.get_total():.2f}")

register.clear()
