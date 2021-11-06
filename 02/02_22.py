import random

computer_roll = random.randint(1, 6)
user_bet = int(input("Guess the value:"))

if user_bet == computer_roll:
    print("Correct")
else:
    print("Wrong")
