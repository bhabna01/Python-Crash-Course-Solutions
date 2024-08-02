sandwitch_orders=['chicken','turkey','tuna','pastrami','roast beef','pastrami','pastrami']
print("The deli ran out of pastrami")
while 'pastrami' in sandwitch_orders:
    sandwitch_orders.remove('pastrami')
print(sandwitch_orders)