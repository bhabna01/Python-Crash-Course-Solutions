rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China",
    "Mississippi": "United States",
    "Ganges": "India"
}
for key,value in rivers.items():
    print(f"{key} runs through {value}")
print("The rivers in this dictionary are:")
for key in rivers.keys():
    print(key)
print("The countries in this dictionary are:")
for value in rivers.values():
    print(value)