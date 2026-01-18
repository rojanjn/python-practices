# Expense Tracker Functions
from datetime import datetime
import csv
import os

# CSV file functions
CSV_FILE = "expense-tracker/expenses/expenses.csv"

def load_from_csv():
    expenses = []

    if not os.path.exists(CSV_FILE):
        return expenses

    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append({
                "id": int(row["id"]),
                "category": row["category"],
                "amount": float(row["amount"]),
                "date": row["date"]
            })   
    return expenses

def save_to_csv(expenses):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["id", "category", "amount", "date"]
        )

        writer.writeheader()
        writer.writerows(expenses)

# COLORS
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# main functions
def _parse_date(date_str: str) -> datetime:
    date_str = date_str.strip()
    parts = date_str.split("-")

    if len(parts) !=3:
        raise ValueError("Date must be in YYYY-MM-DD format.")

    y, m, d = parts
    normalized = f"{int(y):04d}-{int(m):02d}-{int(d):02d}"    
    
    return datetime.fromisoformat(normalized)

def add_expense(expenses, category, amount, date_str):
    if not expenses:
        new_id = 1
    else:
        new_id = expenses[-1]["id"] + 1

    expenses.append({
        "id": new_id,
        "category": category,
        "amount": float(amount),
        "date": date_str
    })
    save_to_csv(expenses)

    print(f"\n{GREEN}=== Expense added with ID {new_id}{RESET}")

def update_expense(expenses, expense_id, category=None, amount=None, date=None):
    for exp in expenses:
        if exp["id"] == expense_id:
            if category is not None:
                exp["category"] = category
            if amount is not None:
                exp["amount"] = float(amount)
            if date is not None:
                exp["date"] = date

            save_to_csv(expenses)
            print(f"\n{GREEN}=== Expense updated.{RESET}")
            return
        
    print(f"\n{RED}=== Expense not found.{RESET}")

def delete_expense(expenses, expense_id):
    for exp in expenses:
        if exp["id"] == expense_id:
            expenses.remove(exp)
            
            save_to_csv(expenses)
            print(f"\n{GREEN}=== Expense deleted.{RESET}")
            return
        
    print(f"\n{RED}=== Expense not found.{RESET}")

def view_all(expenses):
    if not expenses:
        print(f"\n{YELLOW}=== No expenses yet.{RESET}")
        return
    
    total = 0.0
    print("\n--- All expenses ---")

    for exp in expenses:
        print(
            f'\nID {exp["id"]} || {exp["date"]} || '
            f'{exp["category"]} || ${exp["amount"]:.2f}'
        )
        total += exp["amount"]

    print(f"Total: ${total:.2f}")

def view_month(expenses, inp_month):
    total = 0.0
    found = False

    print(f"\n--- Expenses for Month {inp_month} ---")
    for exp in expenses:
        exp_date = _parse_date(exp["date"])
        
        if exp_date.month == inp_month:
            print(
                f'\nID {exp["id"]} | {exp["date"]} | '
                f'{exp["category"]} | ${exp["amount"]:.2f}'
            )
            total += exp["amount"]
            found = True

    if not found:
        print(f"{YELLOW}=== No expenses for this month.{RESET}")
    else:
        print(f"\nMonthly total: ${total:.2f}")

def set_budget(budget, month, budget_amount):
    budget[int(month)] = float(budget_amount)
    print(
        f"{GREEN}=== Budget set for month {month}: "
        f"${float(budget_amount):.2f} ==={RESET}"
    )  

def _month_total(expenses, month):
    total = 0.0
    for exp in expenses:
        exp_date = _parse_date(exp["date"])

        if exp_date.month == month:
            total += exp["amount"]
    return total

def show_budget_status(expenses, budget, month):
    month = int(month)
    if month not in budget:
        print(f"{YELLOW}No budget set for that month.{RESET}")
        return

    spent = _month_total(expenses, month)
    bud = budget[month]

    print(f"Month {month}: spent ${spent:.2f} / budget ${bud:.2f}")
    if spent > bud:
        print(f"\n{YELLOW}WARNING: You exceeded your budget!{RESET}")

def over_budget(expenses, budget, date_str):
    month = _parse_date(date_str).month
    
    if month not in budget:
        return

    spent = _month_total(expenses, month)
    bud = budget[month]

    if spent > bud:
        print(
            f"\n{YELLOW}WARNING: Month {month} is over budget! "
            f"(${spent:.2f} > ${bud:.2f}){RESET}"
        )