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


def get_expense(user_id):
    cur.execute(
        f"SELECT food, transport, clothes, communications, money_transfer, apartments, gos_uslugi, auto, restaurant, other "  
        f"FROM expenses "
        f"WHERE user_id = {user_id} "
        )
    sum = 0
    for res in cur.fetchall():
        for res_1 in res:
            if res_1 != None:
                sum += res_1
    return sum

