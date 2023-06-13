# Dice Simulator

import random

print("hi is this is a dice simulator by shook-s")
roll_yes_no = input("Do you want to roll the dice? Y/N\n")

while True:
    roll_yes_no = input("Do you want to roll the dice? Y/N\n")
    if roll_yes_no in ["1","y","Y","2","n","N"]:
        if roll_yes_no in ["1","y","Y"]:
            roll_yes_no = "Y"
            break
        else:
            roll_yes_no = "N"
            break
    else:
        print("You didn't pick yes or no")

if roll_yes_no == "Y":
    rolling = random.random(1,6)
    print(rolling)



# For the future I want to do multiple rolls and it would print said outputs