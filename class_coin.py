import cbpro

# inti cbpro client
public_client = cbpro.PublicClient()


class Coin:
    def __init__(self, name):
        self.name = name
        self.ticker = public_client.get_product_ticker(name)
        self.price = self.ticker['price']
