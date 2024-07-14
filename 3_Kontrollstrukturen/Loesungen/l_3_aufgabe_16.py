import random

attempts = 0
number = 0

while number != 7:
    number = random.randint(1, 10)
    attempts += 1

print("Number of attempts:", attempts)
