#money_keeper

import sqlite3

conn = sqlite3.connect('expenses.db')
cur = conn.cursor()


def add_expense_and_category_to_db(message, find_cat, user_id):
    cur.execute(
        f"INSERT INTO expenses"
        f"({find_cat}, user_id)"
        f"VALUES (?, ?)", (f"{message}", f"{user_id}")
        )
    conn.commit()


def get_expense(category, user_id):
    cur.execute(
        f"SELECT {category} "
        f"FROM expenses "
        f"WHERE user_id = {user_id} "
        )
    sum = 0
    for categories_list in cur.fetchall():
        for element_categories in categories_list:
            if element_categories != None:
                sum += element_categories
    return sum

#get_expense('food','387448139')


