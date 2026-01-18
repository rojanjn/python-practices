import argparse as ar
from expenses import funcs

while True:
    print("1. Add expense")
    print("2. Update expense")
    print("3. Delete expense")
    print("4. View expenses")

    choice = input("Please choose between 1 to 4: ")

    if choice == 4:
        print("1. View specific date")
        print("2. View all")
        print("3. exit to the main menu")
        view_choice = input("Please choose between 1 to 3: ")

    
