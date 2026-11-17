#!/usr/bin/env python3
# Created By: Sam V
# Date: Nov 17, 2026
# This program is a number guessing game that continues to prompt the user
# until they guess the correct number, with input validation to handle non-integer inputs and out-of-range guesses.

import random


def main():
    # Generate a random number between 0 and 9
    random_number = random.randint(0, 9)

    print("Welcome to the Random Number Guessing Game!")
    print("I have selected a number between 0 and 9. Try to guess it!")

    # Keep asking until the user guesses correctly
    while True:
        user_input = input("Enter your guess: ")
        try:
            user_guess = int(user_input)
            if not 0 <= user_guess <= 9:
                print("Please enter a number between 0 and 9.")
                continue

            if user_guess == random_number:
                print("You Guessed Correctly!")
                break
            else:
                print("You Guessed Wrong. Try again!")
        except ValueError:
            print(f"{user_input} is not an integer.")


if __name__ == "__main__":
    main()
