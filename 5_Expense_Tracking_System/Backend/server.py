from fastapi import FastAPI, HTTPException
from datetime import date
import db_connector as db
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Expense(BaseModel):
    expense_date: date
    amount: float
    category: str
    notes: str

class DataRange(BaseModel):
    startdate : date
    enddate : date

@app.get('/expenses/{expense_date}', response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve data from database")

    return expenses

@app.post('/expenses/{expense_date}')
def update_expenses(expense_date: date, expenses:list[Expense]):
    db.delete_expenses_for_date(expense_date)
    for expense in expenses:
        expenses = db.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    
    return {'message' : 'Expenses updated successfully'}


@app.post('/analytics')
def get_analytics(data_range: DataRange):
    summary = db.fetch_expense_summary(data_range.startdate, data_range.enddate)
    if summary is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve summary from database")

    response = {}
    total = sum([raw['total'] for raw in summary])
    for row in summary:
        percentage = (row['total']/total)*100 if total != 0 else 0
        response[row['category']] = {
            "total": row['total'],
            "percentage" : round(percentage, 2)
        }

    return response

@app.get('/monthly_analytics')
def monthly_analysis():
    response = db.fetch_monthly_summary()
    if response is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve data from database")

    return response