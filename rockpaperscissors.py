#imports
import random

#functions
def get_player_choice():
    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return player_choice

def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        return "win"
    else:
        return "loss"

#play again loop
play_again = True
while play_again == True:

    #welcome and and ask for number of rounds
    print("Welcome to Rock, Paper, Scissors!")
    input_rounds = int(input("How many rounds would you like to play? Please choose an odd number: ")).strip().lower()
    while input_rounds % 2 == 0 or input_rounds <= 0:
        print("Invalid input. Please choose a positive, ODD number of rounds.")
        input_rounds = int(input("How many rounds would you like to play? Please choose an odd number: ")).strip().lower()

    #set variables to 0
    rounds_played = 0
    computer_score = 0
    player_score = 0

    #gameplay
    while rounds_played < input_rounds:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"The computer chose: {computer_choice}")
        winner = determine_winner(player_choice, computer_choice)
        if winner == "tie":
            print("There is a tie! No points awarded. Try again...")
            continue
        elif winner == "win":
            print(f"{player_choice} beats {computer_choice}. You win!")
            player_score += 1
        else:
            print(f"{computer_choice} beats {player_choice}. Computer wins!")
            computer_score += 1
        rounds_played += 1

    #print game summary + play again option
    print(f"Final Score - You: {player_score}, Computer: {computer_score}")
    if player_score > computer_score:
        print("You win! Good job!")
    else:
        print("Computer wins! GG.")
    play_again_option = input("Would you like to play again? (y/n): ").lower()
    if play_again_option == "y":
        play_again = True
    else:
        play_again = False
        print("Thanks for playing!")
