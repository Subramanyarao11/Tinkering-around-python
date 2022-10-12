import random

roll = random.randint(1,6)
# print(roll);
guess = int(input("Guess the dice roll\n"))
if(guess == roll):
    print("Correct! Computer also rolled a " + str(roll))
else:
    print("Wrong! Computer rolled a " + str(roll))
