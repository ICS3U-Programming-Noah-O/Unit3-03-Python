#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Dec. 9, 2021
# This program allows a user to guess a number between
# 0 and 9 when the initial number is randomly generated

import colorama
import random
import time
from colorama import Fore, Back, Style


def main():
    # This function asks for the users number and
    # then compares it to the constant

    # Randomly generate the number
    rand_num = random.randint(0, 9)

    # Input
    print(Fore.WHITE + "I have picked a number between 0 and 9.")
    time.sleep(1)
    print(Fore.WHITE + "Guess my number!!!")
    print(Fore.BLUE + " ")
    user_num = int(input("Enter your guess: "))

    # Process/Output
    time.sleep(1)
    print(Fore.CYAN + " ")
    if user_num == rand_num:
        print("You guessed it! Most impressive.")
    else:
        print("Sorry, that is incorrect. The number was: {}.".format(rand_num)
              + " Try again")
        print("")
        time.sleep(1)
        main()


if __name__ == "__main__":
    main()
