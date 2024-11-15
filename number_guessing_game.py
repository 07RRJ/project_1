import os           # important stuff for the code to work and look neeter
import random
from colors import bcolors
os.system("cls")

the_random_number = 0          # needed variables
your_guess_hig_low = ""
wanna_play_again = "yes"

while True:            # the whole program loop

    the_random_number = random.randint(1, 100)          #refreshing some of the needed variables so you can play again
    your_guess = 0
    your_guess_hig_low = ""
    tries_left = 7

    print(bcolors.CYAN, " " * 4, "=" * 35, bcolors.DEFAULT)            # welcome text
    print(bcolors.CYAN, " " * 4, "=" * 3, bcolors.PURPLE, "GUESS THE NUMBER 1 TO 100", bcolors.CYAN, "=" * 3)
    print(bcolors.CYAN, " " * 4, "=" * 35, bcolors.DEFAULT, "\n")
    print(bcolors.UNDERLINE + "use \"Q\" or any number below 1 to quit" + bcolors.DEFAULT)

    while tries_left > 0:         # the game loop + your guess input
        your_guess = input(f"\n{your_guess_hig_low}what do you think the random number is? ")
        if your_guess.isdigit():
            your_guess = int(your_guess)
            if your_guess > 100:
                print(f"\n{bcolors.RED}{bcolors.UNDERLINE}pwwese guess below 101 to guess{bcolors.DEFAULT}")
                your_guess_hig_low = "so "
            elif your_guess <= 0:
                print("you quit the game")
                break
            else:
                if your_guess > the_random_number:          # the game loop + logic if you win, quit or lose
                    tries_left -= 1
                    print(f"you have {tries_left} tries left")
                    your_guess_hig_low = bcolors.RED + "your guess was to high, " + bcolors.DEFAULT
                elif your_guess < the_random_number:
                    tries_left -= 1
                    print(f"you have {tries_left} tries left")
                    your_guess_hig_low = bcolors.BLUE + "your guess was to low, " + bcolors.DEFAULT
                elif your_guess == the_random_number:
                    break
        elif your_guess.lower() == "q":
            break
        else:
            print(f"\n{bcolors.RED}{bcolors.UNDERLINE}use numbers 1-100 to guess, anything below 1 or \"q\" to quit{bcolors.DEFAULT}")

    if your_guess == the_random_number:          # did you win or lose
        print(f"{bcolors.GREEN}\n\ncorrect(= \nyou won, congrats with {tries_left} tries_left to spare \n{bcolors.DEFAULT}")
    else:
        print(f"{bcolors.BRIGHT_RED} \nYou lose BOZO {bcolors.DEFAULT} \nthe random number was {bcolors.BRIGHT_RED}\"{the_random_number}\"\n {bcolors.DEFAULT}")

    wanna_play_again = input(f"do you want to play again,{bcolors.GREEN} \"y\"{bcolors.DEFAULT} to play again and {bcolors.BRIGHT_RED}anything else {bcolors.DEFAULT}to stop \n").lower()           # this is if you want to start again if you won/lost/quit 
    if wanna_play_again != "y":
        print(f"\n   {bcolors.UNDERLINE}you left the game{bcolors.DEFAULT}\n")
        break
    else:
        os.system("cls")