#Rock paper scissor Game

import random
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
choices = (ROCK,PAPER,SCISSORS) #tuple do not allow the modifications


def get_user_choice():
    while True: #infinite loop untill the user stop playing
        user_choice = input("Rock, Paper, or Scissors? :(r/p/s) ").lower()
        if user_choice in choices: #check if the user choosen correct option or not if not display the below error message
            return user_choice
        else:
            print("Invalid choice!!")

def display_choices(user_choice,computer_choice):
    print(f"you choose '{user_choice}'") #prints the what user have choosen
    print(f"computer choose '{computer_choice}'") #prints the what computer have choosen
    

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        print("Tie")
    elif ( #it is an efficient way to check 3 conditions in one if condition statement
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)):
        print("You win!")
    else:
        print("You loose")


def play_game():

    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices) #computer randomly chooses the option

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("continue? (y/n): ").lower()
        if should_continue == 'n':
            break 

play_game()