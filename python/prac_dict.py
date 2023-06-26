import json

person_file_path = "/Users/aarush/Documents/git/training/python/person.json"

person_file = open(person_file_path, "r")

person = json.load(person_file)

person_file.close()

print("printing all the root keys in the dictionary")
for info in person:
    print(info)
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

#person["friends"].append("Dhruv")
person["hobbies"].append("cricket")

# Save dictionary in a json file
file_path = "person.json"
json.dump(person, open(file_path, "w"), indent=4)

