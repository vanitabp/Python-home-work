import random

number = int(input("How many dice do you want to roll? : "))

total = 0

for i in range(number):
    dice = random.randint(1, 6)
    print("Dice: ", dice)
    total = total + dice
print("Sum of dice: ", total)