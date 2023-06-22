import json

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

# Get the amount earned for each subject and add it to the total amount earned
for subject in ixl["subjects"]:
    amount = (
        ixl["subjects"][subject]["payment-rate"]
        * ixl["subjects"][subject]["items-completed"]
    )
    amount_earned += amount
print("amount-earned", amount_earned)

# The total amount received
amount_received = 0

# Get the payment received on each date and add it to the total amount received
for date in ixl["payments"]:
    amount = ixl["payments"][date]
    amount_received += amount
print("amount-received", amount_received)

# The total amount due
print("balance amount", round(amount_earned - amount_received, 2))
