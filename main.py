import cbpro
import sqlite3
import datetime
import time

# init cbpro client
public_client = cbpro.PublicClient()

# init db connection and cursor
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# get xlm price in usd
ticker = public_client.get_product_ticker('XLM-USD')

# get current time
current_time_stamp = round(time.time() * 1000)
current_time_readable = datetime.datetime.now().strftime('%H:%M:%S %Y-%m-%d')

# add current price and time to db
cursor.execute('''UPDATE sample_rsi 
                SET price = ?, time = ?, timestamp = ?  
                WHERE timestamp = (SELECT MIN(timestamp) FROM sample_rsi)''',
               [ticker['price'], current_time_readable, current_time_stamp])


# Query db to fetch current price and past 14 prices
cursor.execute("SELECT * FROM sample_rsi ORDER BY timestamp ASC")
prices = cursor.fetchall()


# def calculate_rsi(priceTuple):
#   up_prices = []
#   down_prices = []
#   i = 1

#   while i < len(priceTuple):
#     change = round(priceTuple[i][0] - priceTuple[i-1][0], 6)
#     percent_change = round(change/priceTuple[i-1][0] * 100, 2)
#     if percent_change > 0:
#       up_prices.append(percent_change)
#     elif percent_change < 0:
#       down_prices.append(percent_change)
#     # print(percent_change)
#     i+= 1

#   avg_gain = round(sum(up_prices)/14, 2)
#   avg_loss = abs(round(sum(down_prices)/14, 2))
#   print(up_prices)
#   print(down_prices)
#   print(avg_gain)
#   print(avg_loss)


# calculate_rsi(prices)

print(ticker)

conn.commit()
conn.close()
