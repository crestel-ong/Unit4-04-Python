#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: October 2021
# This program the perfect guessing game

import random


def main():
    # this function sees if you can guess the number

    # this is the where the random number is generated from
    computer_number = random.randint(0, 10)

    # input
    guess_number_as_string = input("Enter a number between 0 - 10: ")

    try:
        # convert string to integer
        guess_number = int(guess_number_as_string)

        # process and output
        while True:
            if guess_number == computer_number:
                print("Great job, you guessed right!")
                break
            elif guess_number < computer_number:
                print("Wrong, try guessing a higher number!")
                print("")
            elif guess_number > computer_number:
                print("Wrong, try guessing a lower number!")
                print("")
            guess_number_as_string = input("Please enter a new guess: ")
            guess_number = int(guess_number_as_string)
    except Exception:
        print("{0} is an invalid input.".format(guess_number_as_string))

    print("\nDone.")


if __name__ == "__main__":
    main()
