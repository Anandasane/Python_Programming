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

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Title line: 30 characters, centered
        title = f"{self.name:*^30}"
        lines = [title]

        # Ledger entries
        for entry in self.ledger:
            desc = entry["description"][:23]
            amount = f"{entry['amount']:.2f}"
            # Right-align amount to 7 characters
            lines.append(f"{desc:<23}{amount:>7}")

        # Total
        total = f"{self.get_balance():.2f}"
        lines.append(f"Total: {total}")

        return "\n".join(lines)


def create_spend_chart(categories):
    # Calculate total spent per category (withdrawals only)
    spent = []
    for cat in categories:
        spent_cat = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent.append(spent_cat)

    total_spent = sum(spent)
    percentages = []
    for s in spent:
        if total_spent == 0:
            percentages.append(0)
        else:
            p = int((s / total_spent) * 100)
            p = (p // 10) * 10
            percentages.append(p)

    chart = "Percentage spent by category\n"

    # Y-axis from 100 to 0
    for i in range(100, -1, -10):
        line = f"{i:>3}|"
        for p in percentages:
            if p >= i:
                line += " o "
            else:
                line += "   "
        # Add one extra space to have exactly two spaces after the final bar
        line += " "
        chart += line + "\n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "    "
        for cat in categories:
            if i < len(cat.name):
                line += " " + cat.name[i] + " "
            else:
                line += "   "
        # Add one extra space to have exactly two spaces after the final category
        line += " "
        chart += line + "\n"

    # Remove the final newline (as required)
    return chart.rstrip("\n")

food = Category('Food')

food.deposit(1000, 'initial deposit')
print(food.get_balance())
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and food')
clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
# Outputs the formatted ledger

print(create_spend_chart([food, clothing]))
# Outputs the bar chart