# Expense Tracker Functions
from datetime import datetime

def _parse_date(date_str: str) -> datetime:
    return datetime.fromisoformat(date_str)

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

    print(f"\n===== Expense added with ID {new_id}")

    expenses.append(expenses)

def update_expense(expenses, expense_id, category=None, amount=None, date=None):
    for exp in expenses:
        if exp["id"] == expense_id:
            if category is not None:
                exp["category"] = category
            if amount is not None:
                exp["amount"] = float(amount)
            if date is not None:
                exp["date"] = date

            print("\n===== Expense updated.")
            return
        
        print("\n===== Expense not found.")

def delete_expense(expenses, expense_id):
    for exp in expenses:
        if exp["id"] == expense_id:
            expenses.remove(exp)
            
            print("\n===== Expense deleted.")
            return
        
    print("\n===== Expense not found.")

def view_all(expenses):
    if not expenses:
        print("\n===== No expenses yet.")
        return
    
    total = 0.0
    print("\n--- All expenses ---")

    for exp in expenses:
        print(f'ID {exp["id"]} || {exp["date"]} || {exp["category"]} || ${exp["amount"]:.2f}')

    print(f"Total: ${total:.2f}")

def view_month(expenses, inp_month):
    total = 0.0
    found = False

    print(f"\n--- Expenses for Month {inp_month} ---")
    for exp in expenses:
        exp_date = _parse_date(exp["date"])
        
        if exp_date.inp_month == inp_month:
            print(f'ID {exp["id"]} | {exp["date"]} | {exp["category"]} | ${exp["amount"]:.2f}')
            total += exp["amount"]
            found = True

    if not found:
        print("===== No expenses for this month.")
    else:
        print(f"\nMonthly total: ${total:.2f}")

def set_budget(budget, month, budget_amount):
    budget[int(month)] = float(budget_amount)
    print(f"===== Budget set for month {month}: ${float(budget_amount):.2f}")

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
        print("No budget set for that month.")
        return

    spent = _month_total(expenses, month)
    bud = budget[month]

    print(f"Month {month}: spent ${spent:.2f} / budget ${bud:.2f}")
    if spent > bud:
        print("\n=====WARNING: You exceeded your budget!=====")

def over_budget(expenses, budget, date_str):
    # called after adding/updating an expense
    inp_month = _parse_date(date_str).inp_month
    if inp_month not in budget:
        return

    spent = _month_total(expenses, inp_month)
    bud = budget[month]
    if spent > bud:
        print(f"⚠ WARNING: Month {inp_month} is over budget! (${spent:.2f} > ${bud:.2f})")