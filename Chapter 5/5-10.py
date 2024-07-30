current_users=["bhabna",'ankhi',"orpy","lubna","kusum"]
new_users=["Ritu",'Ankhi',"Orpy","Arnab","Tuli"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("The name has been used")
    else:
        print("The user name is available")
