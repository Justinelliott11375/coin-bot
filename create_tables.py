import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE sample_rsi (
                coin TEXT,
                price REAL,
                time TEXT,
                timestamp INTEGER
            )""")

cursor.execute("""CREATE TABLE orders (
                coin TEXT,
                type TEXT
                price REAL,
                time TEXT,
                timestamp INTEGER
            )""")

conn.commit()

conn.close()
