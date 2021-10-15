
# This file called "random" will help to create a random number
import random


def randomNumber():
    randomInteger = random.randint(1,6)
    print("You rolled a ", randomInteger)


def main():

    playAgain = "Y"

    print("WELCOME TO THE DICE ROLLING GAME!!!")

    # As long as the user wants to play again
    while(playAgain == "Y"):

        print("\nBeginning roll....")

        randomNumber()      # generate a random number

        # Ask the player if they want to play again
        playAgain = input("\nDo you want to play again (Y/N)?  ")
        playAgain = playAgain.upper() # Uppercase the answer

        # If the player enters an invalid choice
        while (playAgain != "Y" and playAgain != "N"):

            print("Invalid choice: Choose (Y/N)\n")
            playAgain = input("\nDo you want to play again?  ")
            playAgain = playAgain.upper()



    print("\nThanks for playing!")


main()




