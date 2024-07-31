fav_number={
    "Bhabna":"C++",
    "Lubna":"C",
    "Kusum":"Python",
    "Ankhi":"Ruby",
    "Orpy":"JS"
}
poll=['Bhabna','Kusum','Ritu','Minhaj','Afrin',"Yousuf"]

for name in poll:
    if name in fav_number.keys():
        print(f"Thank you for responding {name}")
    else:
        print(f"You should take the poll {name}")