# Dice Simulator

import random

print("hi is this is a dice simulator by shook-s")

def roll():
    if roll_yes_no == "Y":
        while True:
            try:
                number_of_die = int(input("How many dice do you want to roll?\n"))
                if number_of_die > 0:
                    break
                else:
                    print("Enter a positive number.")
            except ValueError:
                print("Error: Enter a valid number")

        counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        rolls = []

        for _ in range(number_of_die):
            rolling = random.randint(1, 6)
            rolls.append(str(rolling))
            if number_of_die > 10:
                counts[rolling] += 1

        result = ", ".join(rolls)
        print(f"The dice rolls are: [{result}]")

        if number_of_die > 10:
            print("Since you rolled the die a lot..\nHere is what I found out!")
            for number, count in counts.items():
                print(f"{number}s: {count}")

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
