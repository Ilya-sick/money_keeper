#money_keeper

import sqlite3

conn = sqlite3.connect('expenses.db')
cur = conn.cursor()


def add_expense_and_category_in_db(message, find_cat):
    
    cur.execute(
        f"INSERT INTO expenses"
        f"({find_cat})"
        f"VALUES ({message})"
        )
    conn.commit()