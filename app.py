#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# write a rock paper scissors game

import random

# Define the choices for Rock, Paper, and Scissors
choices = ["Rock", "Paper", "Scissors"]

# Function to get the user's choice
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "Rock" and computer_choice == "Scissors") or \
       (user_choice == "Paper" and computer_choice == "Rock") or \
       (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    return "Computer wins!"

# Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}, and the computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Thanks for playing!")
