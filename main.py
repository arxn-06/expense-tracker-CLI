import json
import os

FILE_NAME = "expenses.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return {"income": [], "expenses": []}

def save_data(data):
    with open(FILE_NAME, 'w') as f:
        json.dump(data, f, indent=2)

def add_income(amount, description):
    data = load_data()
    data["income"].append({"amount": amount, "description": description})
    save_data(data)
    print(f"Added income: {amount} - {description}")

def add_expense(amount, description):
    data = load_data()
    data["expenses"].append({"amount": amount, "description": description})
    save_data(data)
    print(f"Added expense: {amount} - {description}")

def get_balance():
    data = load_data()
    total_income = sum(item["amount"] for item in data["income"])
    total_expense = sum(item["amount"] for item in data["expenses"])
    return total_income - total_expense

def show_summary():
    data = load_data()
    print("Summary:")
    print("Income:")
    for i, item in enumerate(data["income"], 1):
        print(f"  {i}. {item['description']} - {item['amount']}")
    print("Expenses:")
    for i, item in enumerate(data["expenses"], 1):
        print(f"  {i}. {item['description']} - {item['amount']}")
    print(f"Balance: {get_balance()}")

def main():
    while True:
        print("\nChoose option:")
        print("1) Add Income 2) Add Expense 3) Show Summary 4) Exit")
        choice = input()
        if choice == '1':
            amount = float(input("Enter income amount: "))
            desc = input("Enter description: ")
            add_income(amount, desc)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            desc = input("Enter description: ")
            add_expense(amount, desc)
        elif choice == '3':
            show_summary()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if _name_ == "_main_":
    main()
