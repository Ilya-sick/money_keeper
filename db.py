#money_keeper

from datetime import datetime
import sqlite3

conn = sqlite3.connect('expenses.db')
cur = conn.cursor()


def add_expense_and_category_to_db(message, find_cat, user_id, date_time):
    cur.execute(
        f"INSERT INTO expenses"
        f"({find_cat}, user_id, date_time)"
        f"VALUES (?, ?, ?)", (f"{message}", f"{user_id}", f"{date_time}")
        )
    conn.commit()


def get_expense(category, user_id, date_time):
    cur.execute(
        f"SELECT {category} "
        f"FROM expenses "
        f"WHERE user_id = {user_id} AND date_time > {date_time} "
        )
    sum = 0
    for categories_list in cur.fetchall():
        for element_categories in categories_list:
            if element_categories != None:
                sum += element_categories
    return sum


