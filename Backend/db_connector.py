import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logging

logger = setup_logging('db_connector')


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="username",
        password="pwd",
        database="DBname",
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()
    print("Closing cursor")

    cursor.close()
    connection.close()


def fetch_all_records():
    query = "SELECT * from expenses"

    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        logger.info("fetch_all_record from Expenses")
        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT * FROM expenses WHERE expense_date = %s", (expense_date,)
        )
        expenses = cursor.fetchall()
        logger.info(f"fetch_expenses_for_date called with {expense_date}")
        # for expense in expenses:
        #     print(expense)
        return expenses


def insert_expense(expense_date, amount, category, notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes),
        )
        logger.info(f"insert_expenses_for_date called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")


def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))
        logger.info(f"delete_expenses_for_date called with {expense_date}")

def fetch_expense_summary(start_date, end_date):
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total 
               FROM expenses WHERE expense_date
               BETWEEN %s and %s  
               GROUP BY category;''',
            (start_date, end_date)
        )
        data = cursor.fetchall()
        logger.info(f"fetch_expense_summary called with start: {start_date} end: {end_date}")
        return data

def fetch_monthly_summary():
    with get_db_cursor() as cursor:
        cursor.execute(
            '''select month(expense_date) as month_num,MONTHNAME(expense_date) as month_name,  sum(amount) as total_expenses
                from expenses
                group by month_num, month_name ;'''
        )
        data = cursor.fetchall()
        logger.info(f"fetch_monthly_summary called ")
        return data

if __name__ == "__main__":
    fetch_expenses_for_date("2024-08-02")
