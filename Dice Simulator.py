# Dice Simulator

import random

print("hi is this is a dice simulator by shook-s")

def roll():
    if roll_yes_no == "Y":
        while True:
            try:
                number_of_die = int(input("How many die do you want to roll?\n"))
                if int(number_of_die) == number_of_die:
                    break
            except ValueError:
                print("Error pick a number")

        rolls = []
        for x in range(number_of_die):
            rolling = random.randint(1, 6)
            rolls.append(str(rolling))

        result = ", ".join(rolls)
        print(f"The dice rolls are: [{result}]")
        play_again()

def play_again():    
    roll_again = input("Do you want to roll again? Y/N\n")
    if roll_again in ["1","y","Y","2","n","N"]:
        if roll_again in ["1","y","Y"]:
            roll()
        else:
            print("Bye bye")

while True:
    roll_yes_no = input("Do you want to roll the dice? Y/N\n")
    if roll_yes_no in ["1","y","Y","2","n","N"]:
        if roll_yes_no in ["1","y","Y"]:
            roll_yes_no = "Y"
            roll()
            break
        else:
            print("Bye bye")
            break
    else:
        print("You didn't pick yes or no")
