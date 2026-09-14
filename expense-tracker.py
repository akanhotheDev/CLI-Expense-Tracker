## A CLI Based Expnese Tracker
import json
import os

fileName = "Expense.json"


def add_expense(filepath, expense):
    # check if th file exist and load exist data
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath, "r") as e:
            expenses = json.load(e)
            if not isinstance(expenses, list):
                expenses = [expenses]
    else:
         expenses = []

    # expenses = []

    expenses.append(expense)

    with open(filepath, "w") as f:
        json.dump(expenses, f, indent = 3)

def load_expense():
    # expenses = []

    with open(fileName, 'r') as f:
        return json.load(f)
    


def Expense_Tracker():
    while True:
        status = input("Add an (more) expense? (y/n)(yes/no) or delete one\n").lower()
        if status == "n" or status == "no":
            break
        elif status == "y" or status == "yes":
            ctgry = input("What's the category of your expense?\n")
            try:
                amnt = int(input("What was/is the anount?\n"))
            except ValueError:
                return "Please provide an Integer"
            desc = input("The description?\n")
            expense = {
                "amount": amnt,
                "category": ctgry,
                "description": desc
            }    
            add_expense(fileName, expense)
            expenselist = load_expense()
            total = sum(costs["amount"] for costs in expenselist)
            with open ("totalxpense.json", "w") as t:
                json.dump(total, t)
                    
        else: 
            return "Command not recongnised"
            
        




   
    
       

test = Expense_Tracker()
print(test)