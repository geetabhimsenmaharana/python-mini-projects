# -------------------------------
# DAY 2: NUMBER GUESSING GAME
# -------------------------------

# We need this to generate a random number
import random


# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# This variable will count how many attempts user takes
attempts = 0

print("Welcome to the Guessing Game!")
print("I have selected a number between 1 and 100.")


# Loop will keep running until user guesses correctly
while True:

    try:
        # Take input from user and convert to number
        user_guess = int(input("Enter your guess: "))

        # Increase attempt count
        attempts = attempts + 1

        # Check if guess is correct
        if user_guess == secret_number:
            print("🎉 Correct! You guessed it in", attempts, "attempts.")
            break   # Stop the loop

        # If guess is too high
        elif user_guess > secret_number:
            print("Too high! Try again.")

        # If guess is too low
        else:
            print("Too low! Try again.")

    # Handle invalid input (like text)
    except ValueError:
        print("Please enter a valid number!")


print("Game Over")