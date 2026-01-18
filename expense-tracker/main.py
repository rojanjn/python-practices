import argparse as ar
from expenses import funcs

expenses = []

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. Update expense")
        print("3. Delete expense")
        print("4. View expenses")
        print("5. Set a budget")

        choice = input("Please choose an option: ")

        if choice == "1":
            category = input("Category: ")
            amount = float(input("Amount: "))
            date = input("Date (format: YYYY-MM-dd): ")
            
            funcs.add_expense(expenses, category, amount, date)

        elif choice == "2":
            expense_id = int(input("Enter expense ID to update: "))
            funcs.update_expense(expenses, expense_id)

        elif choice == "3":
            expense_id = int(input("Enter expense ID to delete: "))
            funcs.delete_expense(expenses, expense_id)

        elif choice == "4":
            print("1. View a summary of all")
            print("2. View a summary a specific month")
            view_choice = input("Please choose an option: ")
            
            if view_choice == "1":
                funcs.view_all(expenses)

            elif view_choice == "2":
                inp_month = input("Enter a month you would like to view its expenses: ")

                funcs.view_month(expenses, inp_month)

            elif view_choice == "3":
                print("Exiting to main menu...")
                funcs.menu()
            else:
                print("INVALID INPUT. Try again...")
                break

        else:
            print("INVALID INPUT! Try again...")
            break
        
if __name__ == "__main__":
    main()