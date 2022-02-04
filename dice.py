import random

#Simple dice using while True.
while True:
    print("1. Roll the dice")
    print("2. Exit")
    roll = int(input(">>>:"))
    if roll == 1:
        print(random.randint(1,6))
    elif roll == 2:
        break
        

