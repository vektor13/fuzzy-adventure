#!/usr/bing/python3

## bagels.py

# In Bagels, a deductive logic game, you must guess a secret three-digit
# number based on clues. The game offers one of the following hints in
# response to your guess: “Pico” when your guess has a correct digit in the
# wrong place, “Fermi” when your guess has a correct digit in the correct
# place, and “Bagels” if your guess has no correct digits. You have 10 tries
# to guess the secret number.

import random                                                      

NUM_GUESSES = 3
NUM_DIGITS = 3

def main():
    print("""Bagels is a deductive logic game. By Al Sweigart.
          I am thinking of a {}-digit number with no repeated digits.
          Try to guess what it is. Here are some clues:
          When I say: That means:
          Pico  One digit is correct but in the wrong position.
          Fermi One digit is correct and in the right position.
          Bagels No digit is correct.
          """.format(NUM_DIGITS))

    while numGuesses <= MAX_GUESSES:
        guess = ''
        # Keep looping until they enter a valid guess:
        while len(guess) != MNUM_DIGITS or not guess.isdecimal():
            print('Guess #{}: '.format(numGuesses))
            guess = input('> ')

            break

                
if __name__ == '__main__':
    main()  
