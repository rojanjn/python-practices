# Expense Tracker Functions
from datetime import date
from typing import Any, Dict, List, Optional
# from expenses.csv import CSVHelper
CSV_FILE = 'expenses.csv'
CAP_FILE = 'monthly.csv'

def add_expense(expenses, category, amount, date_str):
    new_id = 

    expense = {
        "id": new_id,
        "category": category,
        "amount": amount,
        "date": date_str
    }
    expenses.append(expenses)
    pass

def update_expense(expenses, id):
    pass

def delete_expense(expenses, id):
    pass

def view_all(expenses):
    pass

def view_month(expenses, inp_month):
    pass

def set_budget(expenses, budget):
    pass
