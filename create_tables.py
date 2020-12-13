import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE sample_rsi (
                price REAL,
                time TEXT,
                timestamp INTEGER
            )""")

conn.commit()

conn.close()
