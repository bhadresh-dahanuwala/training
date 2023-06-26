from random import randint

numbers = []

for i in range(5):
    random_int = randint(1, 10)
    if random_int not in numbers:
        numbers.append(random_int)

print(numbers)