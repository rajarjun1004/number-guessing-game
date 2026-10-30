import random

secret_number = random.randint(1, 100)
attempts = 0

print("================================")
print("      NUMBER GUESSING GAME")
print("================================")
print("I have selected a number between 1 and 100.")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")

        elif guess < secret_number:
            print("Too low! Try a higher number.")

        elif guess > secret_number:
            print("Too high! Try a lower number.")

        else:
            print(f"\nCongratulations! You guessed it!")
            print(f"The number was {secret_number}.")
            print(f"Attempts taken: {attempts}")
            break

    except ValueError:
        print("Invalid input! Please enter a whole number.")