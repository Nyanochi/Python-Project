import random

def new_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print("Welcome to the game of Rock, Paper & Scissors")
    user_choice = input("Please choose Rock, Paper or Scissors: ")
    while user_choice.lower() not in choices:
        print("Invalid input!")
        input("Please choose again. Rock, Paper or Scissors: ")
    print("Computer: ", computer_choice)
    if user_choice.lower() == computer_choice:
        print("It\'s a tie.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        print("You won!")
    else:
        print("You lost!")


new_game()
while True:
    play_again = input("Do you want to play again? ")
    if play_again.lower() == "yes":
        new_game()
    else:
        break
print("See you again!")

