from expenses import funcs

# COLORS
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

expenses = funcs.load_from_csv()
budget = {}

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. Update expense")
        print("3. Delete expense")
        print("4. View expenses")
        print("5. Set a budget")
        print("6. Exit")

        choice = input("Please choose an option: ").strip()

        # add expense
        if choice == "1":
            category = input("Category: ").strip()
            amount = float(input("Amount: ").strip())
            date_str = input("Date (format: YYYY-MM-DD): ").strip()
            
            funcs.add_expense(expenses, category, amount, date_str)
            funcs.over_budget(expenses, budget, date_str)

        # update expense
        elif choice == "2":
            expense_id = int(input("Enter expense ID to update: ").strip())
            print("What do you want to update?")
            print("1. Category")
            print("2. Amount")
            print("3. Date")

            update_choice = input("Choose an option: ").strip()

            # updating the category
            if update_choice == "1":
                new_category = input("New category: ").strip()
                funcs.update_expense(expenses, expense_id, category=new_category)

            # updating the amount
            elif update_choice == "2":
                new_amount = float(input("New amount: ").strip())
                funcs.update_expense(expenses, expense_id, amount=new_amount)

            # updating the date
            elif update_choice == "3":
                new_date = input("New date (YYYY-MM-DD): ").strip()
                funcs.update_expense(expenses, expense_id, date_str=new_date)
                funcs.over_budget(expenses, budget, new_date)

            else: 
                print(f"{RED}INVALID INPUT! Try again...{RESET}")

        # delete expense
        elif choice == "3":
            expense_id = int(input("Enter expense ID to delete: ").strip())
            funcs.delete_expense(expenses, expense_id)

        # view expenses
        elif choice == "4":
            print("\n--- View Expenses ---")
            print("1. View a summary of all")
            print("2. View a summary a specific month")
            print("3. Back")

            view_choice = input("Please choose an option: ").strip()
            
            # view a summary of all expenses
            if view_choice == "1":
                funcs.view_all(expenses)

            # view a summary of a specific month's expenses
            elif view_choice == "2":
                inp_month = int(input("Enter month (1-12): ").strip())
                funcs.view_month(expenses, inp_month)

            # back to the main menu
            elif view_choice == "3":
                continue
            
            else:
                print(f"{RED}INVALID INPUT! Try again...{RESET}")

        # set a monthly budget
        elif choice == "5":
            month = int(input("Month (1-12): ").strip())
            budget_amount = float(input("Budget amount: ").strip())
            
            funcs.set_budget(budget, month, budget_amount)
            funcs.show_budget_status(expenses, budget, month) 

        # exiting the app
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print(f"{RED}INVALID INPUT! Try again...{RESET}")
        
if __name__ == "__main__":
    main()