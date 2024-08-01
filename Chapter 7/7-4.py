
prompt="Enter 'quit to end the program "
prompt+="\nEnter Pizza Toppings of your choice:"
toppings=''
while(toppings!='quit'):
    toppings=input(prompt)
    if toppings!='quit':
      print(f"Adding {toppings} in your pizza")
