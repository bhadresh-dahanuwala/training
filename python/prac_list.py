from random import choice

"""
The function will ask the user to provide a number.
The function takes the user prompt as a parameter.
Returns the number provided by the user.
"""


def get_number_from_user(msg):
    # Keep asking for user input, until user gives a valid number
    while True:
        num = input(msg).strip()
        if not num.isnumeric():
            print("Oops! Not a number. Try again")
        else:
            num = int(num)
            return num


num = get_number_from_user("Please insert a number to find the factor(s) of:  ")
start_num = get_number_from_user("Please put a starting number:  ")

# List to store the factor(s)
factors = []

# Checks for the factors of the number and adds to the list
for check in range(start_num, num):
    if num % check == 0:
        factors.append(check)


print("Number of factors found:", len(factors))

# Proceed only if factors found
# Check if the list is not empty
if factors:
    print("Smallest factor found:", min(factors))
    print("Greatest factor found:", max(factors))
    print("Random chosen factor:", choice(factors))
print("List of factors:", factors)
