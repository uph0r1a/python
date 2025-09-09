class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    total_spent = 0
    category_spending = []

    # Calculate spending
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        category_spending.append((category.name, spent))
        total_spent += spent

    # Calculate percentages (rounded down to nearest 10)
    percentages = [
        (name, int((spent / total_spent) * 10) * 10)
        for name, spent in category_spending
    ]

    # Build chart body
    chart = title
    for level in range(100, -1, -10):
        chart += f"{level:>3}|"
        for _, percent in percentages:
            chart += " o " if percent >= level else "   "
        chart += " \n"

    # Separator line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    max_len = max(len(name) for name, _ in percentages)
    for i in range(max_len):
        line = "     "
        for name, _ in percentages:
            line += (name[i] if i < len(name) else " ") + "  "
        chart += line + "\n"

    return chart.rstrip("\n")  # Only strip the final newline


# Example usage
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(1000, "initial deposit")
food.withdraw(200.76, "groceries")

entertainment.deposit(500, "initial deposit")
entertainment.withdraw(300, "concert tickets")

business.deposit(1000, "initial deposit")
business.withdraw(10.5, "stationery")

print(food)
print(create_spend_chart([food, entertainment, business]))
