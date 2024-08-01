prompt="Enter Your age:"
prompt+="\nEnter 'quit to end the program "

while True:
    age=input(prompt)
    if age=='quit':
        break
    else:
        if(int(age)<3):
            print("The ticket is free")
        elif(int(age)<13):
            print("The ticket is 10 dollers")
        else:
            print("The ticket is 15 dollers")
        