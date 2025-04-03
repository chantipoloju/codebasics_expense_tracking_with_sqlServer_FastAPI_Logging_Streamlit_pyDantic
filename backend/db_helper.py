import mysql.connector
from contextlib import contextmanager

##############################

from logging_setup import setup_logger

logger=setup_logger('db_helper', 'server.log')
logger.info("\n")

###########################

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='expense_manager')
    if connection.is_connected():
        print('connection successful')
    else:
        print('NO CONNECTION')
    
    cursor = connection.cursor(dictionary=True)

    yield cursor
    if commit:
        connection.commit()
    
    connection.close()
    cursor.close()

def fetch_all_record():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        return expenses

def fetch_expense_on_date(expense_date):
    logger.info(f"Fetching expenses for date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses where expense_date=%s",(expense_date,))
        expenses = cursor.fetchall()
        return expenses
    
def insert_into_db(expense_date, amount, category, notes):
    logger.info(f"Inserting expense: {expense_date}, {amount}, {category}, {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s,%s,%s,%s)", (expense_date, amount, category, notes))
        expenses = cursor.fetchall()
        return expenses

def delete_expense_from_date(expense_date):
    logger.info(f"Deleting expenses for date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date=%s", (expense_date,))

def fetch_expense_summary(sdate, edate):
    logger.info(f"Fetching expense summary from {sdate} to {edate}")
    with get_db_cursor() as cursor:
        cursor.execute("Select category, sum(amount) as total from expenses where expense_date between %s and %s group by category", (sdate, edate))    
        summary = cursor.fetchall()
        return summary


if __name__ == "__main__":
    expenses = fetch_expense_on_date('2024-08-01')
    print(expenses)
    insert_into_db('2024-08-28', 100, 'Food', 'Lunch')
    expenses = fetch_expense_on_date('2024-08-28')
    print(expenses)
    delete_expense_from_date('2024-08-28')
    expenses = fetch_expense_on_date('2024-08-28')
    print(expenses)
    summary = fetch_expense_summary('2024-08-01', '2024-08-05')
    print(summary)