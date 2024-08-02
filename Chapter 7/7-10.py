responses={}
polling_active=True
while polling_active:
    name=input("\n What's your name?")
    response=input("\nIf you could visit one place in the world where would you visit?")
    responses[name]=response
    repeat=input("Would you like to let another person respond? (yes/no)")
    if repeat=='no':
        polling_active=False
print("-----Polling result-----")
for name,response in responses.items():
    print(f"{name.title()} would like to visit {response}")
