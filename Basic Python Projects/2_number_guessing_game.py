import random

print("Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100")
print("Try to guess it!")

number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Enter your guess: "))
    tries += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {tries} attempts.")
        break

print('Thank you ! Please Play Again')