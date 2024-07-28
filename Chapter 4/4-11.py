pizzas=['peparonni','cheese','tomato']
friends_pizza=pizzas[:]
pizzas.append('alfredo')
friends_pizza.append('buffalo')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friends_pizza:
     print(pizza)