import cbpro
import sqlite3
import datetime
import time
from class_coin import Coin

# init cbpro client
public_client = cbpro.PublicClient()

# init db connection and cursor
conn = sqlite3.connect('database.db')
c = conn.cursor()

# dict to store coin classes
coins = {}

# list of coins to use
coin_names = ['XLM-USD', 'BTC-USD']

# create Coin class for each coin in list
for name in coin_names:
    coins[name] = Coin(name)

# loop to add current coin prices to db
for coin in coins.values():
    # get current time
    current_time_stamp = round(time.time() * 1000)
    current_time_readable = datetime.datetime.now().strftime('%H:%M:%S %Y-%m-%d')

    # check if db has 15 previous prices already stored
    c.execute(
        "SELECT COUNT(*) FROM sample_rsi WHERE coin = ?",
        [coin.name])
    previous_entries = c.fetchall()[0][0]

    if(previous_entries == 15):
        # add current price and time to db
        c.execute('''UPDATE sample_rsi
                        SET coin = ?, price = ?, time = ?, timestamp = ?
                        WHERE timestamp = (SELECT MIN(timestamp) FROM sample_rsi)''',
                  [coin.name, coin.price, current_time_readable, current_time_stamp])
    else:
        c.execute("INSERT INTO sample_rsi VALUES (?, ?, ?, ?)",
                  [coin.name, coin.price, current_time_readable, current_time_stamp])


# # Query db to fetch current price and past 14 prices
# c.execute("SELECT * FROM sample_rsi ORDER BY timestamp ASC")
# prices = c.fetchall()


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

#  print(ticker)

conn.commit()
conn.close()
