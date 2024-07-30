user_names=['Bhabna','Lubna','kusum','admin','Ankhi']
for name in user_names:
    if(name=='admin'):
        print("Hello admin would you like to see status report?")
    else:
        print(f"Hello {name},Thank you for logging in again")
