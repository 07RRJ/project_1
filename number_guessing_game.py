import os           # important stuff for the code to work and look neeter
import random
from colors import bcolors
os.system("cls")

the_random_number = 0          # needed variables
your_guess = 0
tries_left = 7
your_guess_hig_low = ""
wanna_play_again = "yes"

while wanna_play_again == "yes":            # the whole program loop

    the_random_number = random.randint(1, 100)          #refreshing some of the needed variables so you can play again
    your_guess = 0

    print(bcolors.CYAN, " " * 4, "=" * 35, bcolors.DEFAULT)            # welcome text
    print(bcolors.CYAN, " " * 4, "=" * 3, bcolors.PURPLE, "GUESS THE NUMBER 1 TO 100", bcolors.CYAN, "=" * 3)
    print(bcolors.CYAN, " " * 4, "=" * 35, bcolors.DEFAULT, "\n \n")

    while True:         # the game loop
        while True:         # how many tries_left you need
            try:
                tries_left = int(input(f"{bcolors.UNDERLINE} how many tries do you need: {bcolors.DEFAULT}"))
                break
            except:
                print("pwweze use numbers")
        if tries_left <= 0:
            print("you quit the game")
        else:

            while your_guess != the_random_number and tries_left > 0:         # the game loop + your guess input
                while True:
                    try:
                        your_guess = int(input(f"\n{your_guess_hig_low} what do you think the random number is 1-100? "))
                        break
                    except:
                        print("pwwese use a number below 101 for your guess or any number below 1 to quit")
                if your_guess > 100:
                    print("pwwese use a number below 101 for your guess or any number below 1 to quit")
                    your_guess_hig_low = "so"
                else:
                    if your_guess > the_random_number:          # the game loop + logic if you win, quit or lose
                        tries_left -= 1
                        print(f"you have {tries_left} left")
                        your_guess_hig_low = bcolors.RED + "your guess was to high," + bcolors.DEFAULT
                    elif your_guess < the_random_number:
                        tries_left -= 1
                        print(f"you have {tries_left} left")
                        your_guess_hig_low = bcolors.BLUE + "your guess was to low," + bcolors.DEFAULT
        break

    if your_guess == the_random_number:          # did you win or lose
        print(f"{bcolors.GREEN}\n\ncorrect(= \nyou won, congrats in {tries_left} tries_left to spare \n{bcolors.DEFAULT}")
    else:
        print(bcolors.BRIGHT_RED + "\nYou lose BOZO" + bcolors.DEFAULT)

    wanna_play_again = input("do you want to play again, yes for again and anything else to stop \n").lower()           # this is if you want to start again if you won/lost/quit 