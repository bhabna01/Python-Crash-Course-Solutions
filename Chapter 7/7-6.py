prompt="Enter Your age:"
prompt+="\nEnter 'quit to end the program "
age=""
while age!='quit':
    age=input(prompt)
    if(age=='quit'):
        break
    if(int(age)<3):
        print("The ticket is free")
    elif(int(age)<13):
        print("The ticket is 10 dollers")
    else:
        print("The ticket is 15 dollers")