import json

person = {
    "first_name": "Aarush",
    "last_name": "Dahanuwala",
    "dob": "2010-08-30",
    "weight_lbs": {
        "2023-06-15": 95,
        "2023-06-16": 95.2,
        "2023-06-17": 95.3,
        "2023-06-18": 95.4,
    },
    "height_inches": 59,
    "friends": ["Shrirang", "Sid"],
}

"""
print(person["first_name"])

person["weight_lbs"]["2023-06-15"] = 94

for date in person["weight_lbs"]:
    print(date, person["weight_lbs"][date])

for friend in person["friends"]:
    print(friend)
"""
# Create new key in a dictionary
person["hobbies"] = ["soccer"]

# Print all the keys of a dictionary in a loop
for key in person:
    print(key)

# Print all the keys of a dictionary as a list
print(list(person.keys()))

# Print the number of keys in the dictionary
print(len(person.keys()))

# Print the whole dictionary
print(person)

# Save dictionary in a json file
file_path = "person.json"
json.dump(person, open(file_path, "w"), indent=4)
