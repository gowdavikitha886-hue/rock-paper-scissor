
# Day 13: Rock Paper Scissors Game

import random

choices = ["rock", "paper", "scissors"]

while True:

    print("\n===== ROCK PAPER SCISSORS =====")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    user_choice = input("Enter your choice: ").lower()

    if user_choice == "4":
        print("Thanks for playing!")
        print("Day 13 completed!")
        break

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("Your choice:", user_choice)
    print("Computer choice:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a Draw!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: Congratulations! You Win!")

    else:
        print("Result: Computer Wins!")
