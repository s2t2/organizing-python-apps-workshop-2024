# this is the "app/game_loop.py" file (starter v1)...

from random import choice

VALID_OPTIONS = ["rock", "paper", "scissors"]

player_name = input("Please provide a Player Name: ")
print("WELCOME,", player_name, "to my RPS game!")

# GAME LOOP

game_count = 0
win_count = 0

while True:

    user_choice = input("Please choose an option ('rock', 'paper', or 'scissors'): ").lower()
    print("USER CHOSE:", user_choice)

    while user_choice not in VALID_OPTIONS:
        print("INVALID SELECTION. PLEASE TRY AGAIN!")
        user_choice = input("Please choose an option ('rock', 'paper', or 'scissors'): ").lower()
        print("USER CHOSE:", user_choice)

    # only generate computer choice, etc. if user choice is valid!
    computer_choice = choice(VALID_OPTIONS)
    print("COMPUTER CHOSE:", computer_choice)

    # determine outcome:
    if user_choice == computer_choice:
        outcome = "TIE"
    elif user_choice == "rock" and computer_choice == "paper":
        outcome = "LOSE"
    elif user_choice == "rock" and computer_choice == "scissors":
        outcome = "WIN"
    elif user_choice == "paper" and computer_choice == "rock":
        outcome = "WIN"
    elif user_choice == "paper" and computer_choice == "scissors":
        outcome = "LOSE"
    elif user_choice == "scissors" and computer_choice == "rock":
        outcome = "LOSE"
    elif user_choice == "scissors" and computer_choice == "paper":
        outcome = "WIN"

    print("OUTCOME:", outcome)

    # update counters and accumulators
    game_count +=1
    if outcome == "WIN":
        win_count += 1
    print("CURRENT STATS... WINS:", win_count,
        "GAMES:", game_count,
        "WIN PCT:", round(win_count/game_count, 2)
    )

    print("----------------------------")
    play_again = input("Would you like to play again? ('Y' / 'N'): ").upper()
    if play_again == "N":
        print("THANKS FOR PLAYING!")
        break
