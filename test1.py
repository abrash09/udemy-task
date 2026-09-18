import json

expenses = []

def add_expense():
   # request for expense 🤭
    amount = float(input("Enter amount "))
    category = input("Enter category ")
    description = input("Enter description ")
    
    expense = {"amount": amount, "category": category, "description": description }
    expenses.append(expense)
    print("Expense added successfully 😍 \n")

# user view expenses func
def View_all_expenses ():
        if not expenses:
            print("there are no expenses, Enter an expense 🥸")
        else:
            for items in expenses:
                print(f"Amount: {items['amount']} | Category: {items['category']} | Description: {items['description']}")

# calculate total expense func
def calculate_total():
    if not expenses:
         print("No expenses to calculate")
    else:
        total = 0
        for cal_expense in expenses:
             total = total + cal_expense['amount']
        print(f"Total expense balance: ${total}\n")

# saving the saxpenses into a file func
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
    print("Expenses saved successfully!")

# func to load expenses
def load_expenses():
    global expenses
    try:
        with open ("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        pass


load_expenses()  

# func for calculate_by_category
def calculate_by_category():
    if not expenses:
        print("No expenses to calculate")
    else:
        category_totals = {}
        for items in expenses:
            cat = items['category']
            amt = items['amount']
            if cat not in category_totals:
                category_totals[cat] = amt
            else:
                category_totals[cat] += amt
        for category, total in category_totals.items():
                    print(f"{category}: {total}")
        print()  

# func to delete expense
def delete_expense ():
        if not expenses:
            print("No expenses to delete.")
            return 
        for index, item in enumerate(expenses):
            print(f"{index +1}. {item['description']} - {item['amount']}")
        user_choice = int(input("Enter the number of the expense to delete: "))
        final_delete = (user_choice - 1)
        expenses.pop(final_delete)
        print("Expense delete successfully 😍")
              

# lets get the looping started 😁
while True:
    print("1.  Add an expense")
    print("2.  View all expenses")
    print("3. Calculate total spending")
    print("4. Calculate spending by category")
    print("5. delete an expense")
    print("6. Exit")
    choice = input("Enter you preffered choice? ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        View_all_expenses()      
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        calculate_by_category()
    elif choice == "5":
        delete_expense ()
    elif choice == "6":
           save_expenses()
           print("Goodbye!")
           break
    else:
        print("Invalid choice, please try again.\n")
