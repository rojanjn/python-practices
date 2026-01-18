import argparse as ar
from tokenize import Double
from expenses import funcs

while True:
    print("1. Add expense")
    print("2. Update expense")
    print("3. Delete expense")
    print("4. View expenses")
    print("5. Set a budget")

    choice = input("Please choose an option: ")

    if choice == "1":
        category = input("Enter you expense category: ")
        amount = input("Enter the amount: ")
        date = input("Enter the date (format: YYYY-MM-dd): ")

    elif choice == "2":
        

    elif choice == "4":
        while True:
            print("1. View a summary of all expenses")
            print("2. View a summary of expenses for a specific month")
            print("3. exit to the main menu")
            
            view_choice = input("Please choose an option: ")

            if view_choice == "1":
                inp_date = input("Enter a date you would like to view its expenses (format: YYYY-MM-dd): ")
            
            elif view_choice == "2":
                
            elif view_choice == "3":
                print("Exiting to main menu...")
                
            else:
                print("INVALID INPUT. Try again...")
                break

    else:
        print("INVALID INPUT! Try again...")
        break

