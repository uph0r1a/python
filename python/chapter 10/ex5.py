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


items = [
    RetailItem("Jacket", 12, 59.95),
    RetailItem("Designer Jeans", 40, 34.95),
    RetailItem("Shirt", 20, 24.95),
]

for item in items:
    print(
        f"Description: {item.get_description()}\nUnits in Inventory: {item.get_unit()}\nPrice: {item.get_price()}\n"
    )
