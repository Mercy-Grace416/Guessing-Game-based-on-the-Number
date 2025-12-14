import random

number = random.randint(1, 10)
attempts = 0

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print(f"Correct! You guessed it in {attempts} attempts")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")
