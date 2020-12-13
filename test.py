import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM sample_rsi")

print(cursor.fetchall())

conn.commit()
conn.close()
