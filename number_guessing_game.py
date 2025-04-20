#Number Guessing Game

import random

guess_number = random.randint(1,100)
while True:
    try: 
        number = int(input("Guess the number between 1 and 100: "))
        if number > guess_number:
                print("Too High!")
        elif number < guess_number:
                print("Too Low!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number.")

