pets=[]
pet = {
    "name": "Buddy",
    "species": "Dog",
    "breed": "Golden Retriever",
    "age": 5,
    "favorite_toy": "Ball",
    "owner": {
        "name": "Alice",
        "contact": "alice@example.com"
    }
}
pets.append(pet)
# Pet 2
pet = {
    "name": "Whiskers",
    "species": "Cat",
    "breed": "Siamese",
    "age": 3,
    "favorite_toy": "Laser pointer",
    "owner": {
        "name": "Bob",
        "contact": "bob@example.com"
    }
}
pets.append(pet)
# Pet 3
pet = {
    "name": "Nibbles",
    "species": "Hamster",
    "breed": "Syrian",
    "age": 1,
    "favorite_toy": "Wheel",
    "owner": {
        "name": "Carol",
        "contact": "carol@example.com"
    }
}
pets.append(pet)
# Pet 4
pet = {
    "name": "Goldie",
    "species": "Fish",
    "breed": "Goldfish",
    "age": 2,
    "favorite_toy": "Castle",
    "owner": {
        "name": "Dave",
        "contact": "dave@example.com"
    }
}
pets.append(pet)
# Pet 5
pet = {
    "name": "Bella",
    "species": "Dog",
    "breed": "Poodle",
    "age": 4,
    "favorite_toy": "Rope",
    "owner": {
        "name": "Eve",
        "contact": "eve@example.com"
    }
}
pets.append(pet)
for pet in pets:
    print(f"The name of the pet is {pet['name']}.It is a {pet['species']}.It is {pet['age']} year old.It's favorite toy is {pet['favorite_toy']}.It is owned by {pet['owner']['name']}")
    print('\n')