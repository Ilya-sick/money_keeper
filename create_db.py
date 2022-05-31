import sqlite3

conn = sqlite3.connect('expenses.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY,
    id);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS expenses(
    user_id,
    id PRIMARY KEY,
    food,
    transport,
    clothes,
    communications,
    money_transfer,
    apartments,
    gos_uslugi,
    auto,
    restaurant,
    other);
""")