favourite_places = {
    "Alice": ["Paris", "New York", "Tokyo"],
    "Bob": ["London", "Sydney"],
    "Carol": ["Rome", "Barcelona", "Istanbul"]
}
for name , values in favourite_places.items():
    print(f"{name}'s favourite places are:")
    for value in values:
        print(f"{value}")
    print("\n")