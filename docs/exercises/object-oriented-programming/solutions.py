
#from google.colab import userdata
import os
import random


class GameLoop:
    #PLAYER_NAME = userdata.get("PLAYER_NAME")
    PLAYER_NAME = os.getenv("PLAYER_NAME") or "Player One"

    VALID_OPTIONS = ["rock", "paper", "scissors"]

    def __init__(self, game_count=0, win_count=0):
        self.game_count = game_count
        self.win_count = win_count

    @property
    def welcome_message(self):
        return f"WELCOME, {self.PLAYER_NAME} to my RPS game!"


    def prompt_until_valid(self):
        prompt = "Please choose an option ('rock', 'paper', or 'scissors'): "

        user_choice = input(prompt).lower()
        print("USER CHOSE:", user_choice)

        while user_choice not in self.VALID_OPTIONS:
            print("INVALID SELECTION. PLEASE TRY AGAIN!")
            user_choice = input(prompt).lower()
            print("USER CHOSE:", user_choice)

        return user_choice


    def determine_outcome(self, user_choice, computer_choice):
        # there are many ways of doing this
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
        return outcome


    def play(self, user_choice=None, computer_choice=None):
        # passing in default values to allow us to test this function
        # otherwise we capture and generate choices for real

        user_choice = user_choice or self.prompt_until_valid()

        computer_choice = computer_choice or random.choice(self.VALID_OPTIONS)
        print("COMPUTER CHOSE:", computer_choice)

        outcome = game.determine_outcome(user_choice, computer_choice)
        print("OUTCOME:", outcome)

        self.game_count +=1
        if outcome == "WIN":
            self.win_count += 1


    @property
    def win_pct(self):
        try:
            return round(self.win_count / self.game_count, 2)
        except ZeroDivisionError:
            return 0


    def play_until_satisfied(self):
        while True:
            self.play()

            play_again = input("Would you like to play again? ('Y' / 'N'): ").upper()
            if play_again == "N":
                print("THANKS FOR PLAYING!")
                break

        print("----------------------------")
        print("STATS... ")
        print("WINS:", self.win_count)
        print("GAMES:", self.game_count)
        print("WIN PCT:", self.win_pct)



#
# GAME TIME
#

game = GameLoop()
print(game.welcome_message)
game.play()

game = GameLoop()
print(game.welcome_message)
game.play_until_satisfied()



#
# TESTS
#

game = GameLoop()

# WINNER DETERMINATION TESTS:

assert game.determine_outcome("rock", "rock") == "TIE"
assert game.determine_outcome("rock", "paper") == "LOSE"
assert game.determine_outcome("rock", "scissors") == "WIN"
assert game.determine_outcome("paper", "rock") == "WIN"
assert game.determine_outcome("paper", "paper") == "TIE"
assert game.determine_outcome("paper", "scissors") == "LOSE"
assert game.determine_outcome("scissors", "scissors") == "TIE"
assert game.determine_outcome("scissors", "paper") == "WIN"
assert game.determine_outcome("scissors", "rock") == "LOSE"
print("WINNER DETERMINATION TESTS PASS!")

# GAME COUNT TESTS:

game.play("rock", "paper")
assert game.game_count == 1
assert game.win_count == 0
assert game.win_pct == 0

game.play("rock", "paper")
assert game.game_count == 2
assert game.win_count == 0
assert game.win_pct == 0

game.play("rock", "scissors")
assert game.game_count == 3
assert game.win_count == 1
assert game.win_pct == 0.33

print("GAME COUNT TESTS PASS!")
