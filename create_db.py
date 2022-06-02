import sqlite3

conn = sqlite3.connect('expenses.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY,
    id);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS expenses(
    user_id INTEGER,
    id PRIMARY KEY ,
    food INTEGER,
    transport INTEGER,
    clothes INTEGER,
    communications INTEGER,
    money_transfer INTEGER,
    apartments INTEGER,
    gos_uslugi INTEGER,
    auto INTEGER,
    restaurant INTEGER,
    other INTEGER);
""")
