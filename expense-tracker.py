import json
import os

fileName = "Expense.json"


def load_expense(filepath):
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath, "r") as f:
            expenses = json.load(f)
    else:
        expenses = []
    return expenses


def add_expense(filepath, expense):
    expenses = load_expense(filepath)
    expenses.append(expense)
    with open(filepath, "w") as f:
        json.dump(expenses, f, indent=4)
    return expenses


def save_expenses(filepath, expenses):
    with open(filepath, "w") as f:
        json.dump(expenses, f, indent=4)


def Expense_Tracker():
    while True:
        print("1. View existing expense\n2. Add an expense\n3. Calculate total expense\n4. Calculate by category\n5. Delete expense\n6. Exit")
        status = input("Choose your option:\n")

        if status == "1":
            expenses = load_expense(fileName)
            if len(expenses) == 0:
                print("You don't have any expense yet")
            else:
                for expense in expenses:
                    print(f"ID: {expense['id']}")
                    print(f"amount: {expense['amount']}")
                    print(f"category: {expense['category']}")
                    print(f"description: {expense['description']}")
                    print("-" * 20)

        elif status == "2":
            ctgry = input("What is the category of the expense: ")
            amnt = int(input("amount of expense: "))
            desc = input("description of expense: ")

            expenses = load_expense(fileName)
            new_id = max((e["id"] for e in expenses), default=0) + 1

            expense = {
                "id": new_id,
                "amount": amnt,
                "category": ctgry,
                "description": desc
            }

            add_expense(fileName, expense)
            print("Expense added.")
        elif status == "3":
            expenses = load_expense(fileName)
            total = sum(cost["amount"] for cost in expenses)
            print(f"Total: {total}")

        elif status == "4":
            expenses = load_expense(fileName)
            cat = input("Type category: ").strip()
            total = 0
            for cost in expenses:
                if cost["category"] == cat:
                    total += cost["amount"]
            print(f"Total for {cat}: {total}")

        elif status == "5":
            expenses = load_expense(fileName)
            stat = int(input("specify expense id: "))
            new_expenses = [e for e in expenses if e["id"] != stat]

            if len(new_expenses) == len(expenses):
                print("No expense found with that id.")
            else:
                save_expenses(fileName, new_expenses)
                print("Expense deleted.")

        elif status == "6":
            print("Goodbye for now")
            break

        else:
            print("Command not recognised")


Expense_Tracker()