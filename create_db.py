import sqlite3

conn = sqlite3.connect('expenses.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY,
    id);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS expenses(
    user_id PRIMARY KEY,
    food,
    transport,
    clothes,
    communications,
    baby,
    money_transfer,
    apartments,
    pharmacy,
    gos_uslugi,
    auto,
    trip,
    restaurant,
    other);
""")