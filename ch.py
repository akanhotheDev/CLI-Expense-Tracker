import os
import json

fileName = "testing.json"
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

dic ={
     "hkdjf": "hdjdhfj",
     "gfhfej": 23628
}

add_expense(fileName, dic)