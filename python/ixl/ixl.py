import json

# /Users/aarush/Documents/git/training/python/ixl/ixl.py

# Path of ixl.json file
ixl_file_path = "ixl.json"

# Reading the ixl.json file
ixl_file = open(ixl_file_path, "r")

# Loading the json data from the file into a dictionary
ixl = json.load(ixl_file)

# Closing the file
ixl_file.close()

# Total amount earned by completing the topics in all subjects
amount_earned = 0

potential_earning = 0

# Get the amount earned for each subject and add it to the total amount earned
for subject in ixl["subjects"]:
    payment_rate = ixl["subjects"][subject]["payment-rate"]
    total_skills = ixl["subjects"][subject]["total-skills"]
    skills_completed = ixl["subjects"][subject]["skills-completed"]
    pct_completed = round((skills_completed * 100) / total_skills, 2)
    print(f"[{subject}] completed {pct_completed}%")
    amount_earned += payment_rate * skills_completed
    potential_earning += payment_rate + total_skills

print()
print("potential-earnings", potential_earning)
print("amount-earned", amount_earned)
print("percentage-earned", round((amount_earned / potential_earning) * 100, 2))

# The total amount received
amount_received = 0

# Get the payment received on each date and add it to the total amount received
for date in ixl["payments"]:
    amount = ixl["payments"][date]
    amount_received += amount
print("amount-received", amount_received)

# The total amount due
print("balance amount", round(amount_earned - amount_received, 2))
