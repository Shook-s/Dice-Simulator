# Dice Simulator

import random

print("hi is this is a dice simulator by shook-s")

while True:
    roll_yes_no = input("Do you want to roll the dice? Y/N\n")
    if roll_yes_no in ["1","y","Y","2","n","N"]:
        if roll_yes_no in ["1","y","Y"]:
            rolling = random.randint(1, 6)
            print("Rolling...")
            print(f"You got {rolling}!")
            break
        else:
            print("Bye bye")
            break
    else:
        print("You didn't pick yes or no")