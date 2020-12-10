import cbpro

public_client = cbpro.PublicClient()
products = public_client.get_products()

print('hello world')

# for foo in products:
#  print(foo['id'])

print(public_client.get_product_order_book('XLM-USD'))
