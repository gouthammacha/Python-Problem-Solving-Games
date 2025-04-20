#Dice Rolling Game
#Ask: roll the dice?
#If user enters y
    #Generate two random numbers
    #Print them
# If user enters n
    #Print thank you message
    #Terminate
#Else
    #Print invalid choice

import random

#We are using the "while True" to run the loop infinite times untill the user enter "n" option 
while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == 'y':
        die1= random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"{die1,die2}")

#Whenever the user enters the "n" then we are saying to exit the loop by printing the thanks statement and exit the loop with break.
    elif choice == 'n':
        print("Thanks for playing!")
        break #Terminate the program 
    else:
        print("Invalid choice!")