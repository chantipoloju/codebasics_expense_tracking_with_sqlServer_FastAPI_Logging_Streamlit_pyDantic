from fastapi import FastAPI
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

app = FastAPI()

@app.get("/expenses/{expense_date}")
def get_expenses(expense_date: date, response_model=List[Expense]):
    expenses = db_helper.fetch_expense_on_date(expense_date)
    if not expenses:
        return {"message": "No expenses found for this date."}
    return expenses

@app.put("/expenses/{expense_date}")
def update_expense(expense_date: date, expenses: List[Expense]):
    # Delete existing expenses for the given date
    print(expenses)
    db_helper.delete_expense_from_date(expense_date)
    
    # Insert new expenses
    for expense in expenses:
        db_helper.insert_into_db(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "Expenses updated successfully."}
