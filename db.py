#money_keeper

from datetime import date, datetime
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
        f"WHERE user_id = {user_id} AND date_time > {date_time}"
        )
    sum = 0
    for categories_list in cur.fetchall():
        for element_categories in categories_list:
            if element_categories != None:
                sum += element_categories
    return sum

def get_statistics(user_id, category, date_time_start):
    cur.execute(
        f"SELECT {category} "
        f"FROM expenses "
        f"WHERE user_id = {user_id} AND date_time > {date_time_start}"
        )
    sum = 0
    for categories_list in cur.fetchall():
        for element_categories in categories_list:
            if element_categories != None:
                sum += element_categories
    return sum

def find_and_del_last_expense(user_id):
    cur.execute(
        f"SELECT date_time "
        f"FROM expenses "
        f"WHERE user_id = {user_id} "
        f"ORDER BY date_time DESC LIMIT 1"
        ) 
    for delete_this_expense in cur.fetchone():
        cur.execute(
            f"DELETE "
            f"FROM expenses "
            f"WHERE user_id = {user_id} AND date_time = {delete_this_expense}"
        )
        conn.commit()
        return f"Последний расход удален!"

    

    

