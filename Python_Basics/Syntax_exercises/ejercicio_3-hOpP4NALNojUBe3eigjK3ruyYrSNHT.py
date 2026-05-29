import random

# Generate a random integer between 1 and 100
random_number = random.randint(1, 10)
number = int(input("Guess the number between 1 and 10: "))
while number != random_number:
    print("Try again.")
    number = int(input("Guess the number between 1 and 10: "))
print("Congratulations! You guessed the number.")