person1={
    "first_name":"Bhabna",
    "second_name":"Hoque",
    "age":25,
    "city":"Dhaka"
}
person2={
    "first_name":"Lubna",
    "second_name":"Tasnim",
    "age":25,
    "city":"Dhaka"
}
person3={
    "first_name":"Kusum",
    "second_name":"Talukder",
    "age":24,
    "city":"Dhaka"
}
persons=[person1,person2,person3]
for person in persons:
   print(f"{person['first_name']} {person['second_name']} is {person['age']}, lives in {person['city']}")