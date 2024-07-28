my_food=['pizza','falafal','carrot cake']
friends_food=my_food[:]
friends_food.append('chocolate')
print("My favorite foods are:")
for food in my_food:
    print(food)
print("My friend's favorite foods are:")
for food in friends_food:
    print(food)