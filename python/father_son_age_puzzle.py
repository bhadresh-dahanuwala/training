"""

I was 8 and my father was 31
Now my father is double my age.
What is my and my father's age?

"""
son_age = 8
father_age = 31

while True:
    son_age += 1
    father_age += 1
    if son_age * 2 == father_age:
        print(son_age, father_age)
        break