fav_number={
    "Bhabna":[3,2,5],
    "Lubna":[1,2,3,4,5,6],
    "Kusum":[4.45,56,67,78,789],
    "Ankhi":[6,2,3,4,2,1],
    "Orpy":[10,2,33,4,42,2,444]
}
for name,numbers in fav_number.items():
    print(f"{name}'s favorite numbers are")
    for number in numbers:
        print(f"{number}") 
    print('\n')