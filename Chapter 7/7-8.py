sandwitch_orders=['chicken','turkey','tuna','pastrami','roast beef']
finished_sandwiches=[]
while sandwitch_orders:
    finished=sandwitch_orders.pop()
    print(f"I made your {finished} sandwich")
    finished_sandwiches.append(finished)
print("The made sandwiches are:")
for sandwich in finished_sandwiches:
    print("\n",sandwich)
   