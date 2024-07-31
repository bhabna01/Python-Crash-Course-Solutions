# Dictionary storing information about cities
cities = {
    "Paris": {
        "country": "France",
        "population": "2.16 million",
        "facts": "Known as the 'City of Light' and home to the Eiffel Tower."
    },
    "New York": {
        "country": "United States",
        "population": "8.4 million",
        "facts": "Famous for Times Square and the Statue of Liberty."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "facts": "The world's most populous metropolitan area and a major cultural center."
    }
}
for city,city_info in cities.items():
    print("The city name is ",city)
    print("Country:" ,city_info['country'])
    print("Population:",city_info["population"])
    print("Facts:" ,city_info["facts"])
    print("\n")
    
