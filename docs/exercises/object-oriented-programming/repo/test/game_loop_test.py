from app.game_loop import GameLoop

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
