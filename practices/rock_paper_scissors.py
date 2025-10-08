# AC 2nd Rock Paper Scissors

import random

while True:
    options = ["rock", "paper", "scissors"]
    computer_score = 0
    user_score = 0
    user = input("Rock, Paper or Scissors? (Type quit to exit)\n").lower()
    if user =="quit":
        print("Final Score:\nUser Score: {user_score}\nComputer Score: {computer}")
        print("Exiting")
        break
    if user not in options:
        print("Not an option")
        continue
    computer = random.choice(options)
    print(f"\nComputer chose {computer}.\n")
    if user == computer:
        print("Tie\n")
        print(f"User Score: {user_score}\nComputer Score: {computer_score}")
    elif user == "rock" and computer == "scissors":
        print("You Win!\n")
        user_score += 1
        print(f"User Score: {user_score}\nComputer Score: {computer_score}")
    elif user == "scissors" and computer == "paper":
        print("You Win!\n")
        user_score += 1
        print(f"User Score: {user_score}\nComputer Score: {computer}")
    elif user == "paper" and computer == "rock":
        print("You Win!\n")
        user_score += 1
        print(f"User Score: {user_score}\nComputer Score: {computer}")
    else:
        print("You Lost!\n")
        computer_score += 1
        print(f"User Score: {user_score}\nComputer Score: {computer}")

    