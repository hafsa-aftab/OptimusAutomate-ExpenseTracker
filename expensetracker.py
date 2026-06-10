import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add expense
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        category = input("Enter category (Food, Shopping, Travel, Bills): ").strip()

        description = input("Enter description: ").strip()

        date = input("Enter date (YYYY-MM-DD): ").strip()

        # Validate date
        datetime.strptime(date, "%Y-%m-%d")

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("Expense added successfully!")

    except ValueError:
        print("Invalid input! Please enter correct data.")


# View expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\nAll Expenses:\n")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. "
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"Rs.{expense['amount']}"
        )


# Delete expense
def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        index = int(input("Enter expense number to delete: ")) - 1

        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            save_expenses(expenses)

            print(f"Deleted: {removed['description']}")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# Monthly summary
def monthly_summary(expenses):
    if not expenses:
        print("No expenses available.")
        return

    month = input("Enter month (YYYY-MM): ")

    total = 0
    category_totals = {}

    for expense in expenses:
        if expense["date"].startswith(month):

            total += expense["amount"]

            category = expense["category"]

            if category in category_totals:
                category_totals[category] += expense["amount"]
            else:
                category_totals[category] = expense["amount"]

    print(f"\nMonthly Summary for {month}")
    print(f"Total Expenses: Rs.{total}")

    print("\nCategory-wise Expenses:")

    for category, amount in category_totals.items():
        print(f"{category}: Rs.{amount}")


# Main menu
def main():
    expenses = load_expenses()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            delete_expense(expenses)

        elif choice == "4":
            monthly_summary(expenses)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1 to 5.")


main()