
VALID_OPTIONS = ["rock", "paper", "scissors"]

# NOTE: all of these solutions assume valid inputs are being passed in

#
# IF STATEMENT WITH COMPOUND EXPRESSIONS
# (2-18 calculations)
#

def determine_outcome(u, c):
    if u == "rock" and c == "rock":
        return "TIE GAME"
    elif u == "rock" and c == "paper":
        return "COMPUTER WINS"
    elif u == "rock" and c == "scissors":
        return "USER WINS"

    elif u == "paper" and c == "rock":
        return "USER WINS"
    elif u == "paper" and c == "paper":
        return "TIE GAME"
    elif u == "paper" and c == "scissors":
        return "COMPUTER WINS"

    elif u == "scissors" and c == "rock":
        return "COMPUTER WINS"
    elif u == "scissors" and c == "paper":
        return "USER WINS"
    elif u == "scissors" and c == "scissors":
        return "TIE GAME"

    #else:
    #    return "OOPS"


#
# NESTED IF STATEMENT APPROACH:
# (2-6 calculations)
#

def determine_outcome(u, c):
    if u == "rock":
        if c == "rock":
            return "TIE GAME"
        elif c == "paper":
            return "COMPUTER WINS"
        elif c == "scissors":
            return "USER WINS"

    elif u == "paper":
        if c == "rock":
            return "USER WINS"
        elif c == "paper":
            return "TIE GAME"
        elif c == "scissors":
            return "COMPUTER WINS"

    elif u == "scissors":
        if c == "rock":
            return "COMPUTER WINS"
        elif c == "paper":
            return  "USER WINS"
        elif c == "scissors":
            return "TIE GAME"

    #else:
    #    return "OOPS"

#
# IF STATEMENT WITH COMPOUND EXPRESSIONS APPROACH FOR READABILITY, WITH TIES COVERED FIRST:
# (1-8 calculations)
#

def determine_outcome(u, c):
    if u == c:
        return "TIE GAME"
    elif (u == "rock" and c == "scissors") or (u == "paper" and c == "rock") or (u == "scissors" and c == "paper"):
        return "USER WINS"
    else:
        return "COMPUTER WINS" # this assumes valid inputs


#
# TUPLE APPROACH:
# (1-3 calculations)
#

def determine_outcome(u, c):
    # user level, then computer level
    winners = [
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper")
    ]

    if u == c:
        return "TIE GAME"
    elif (u, c) in winners:
        return "USER WINS"
    else:
        return "COMPUTER WINS"



#
# DICTIONARY APPROACH:
# (2 calculations)
#

def determine_outcome(u, c):
    # user level, then computer level
    winners = {
        "rock":{
            "rock": "TIE GAME",
            "paper": "COMPUTER WINS",
            "scissors": "USER WINS",
        },
        "paper":{
            "rock": "USER WINS",
            "paper": "TIE GAME",
            "scissors": "COMPUTER WINS",
        },
        "scissors":{
            "rock": "COMPUTER WINS",
            "paper": "USER WINS",
            "scissors": "TIE GAME",
        },
    }
    outcome = winners[u][c]
    return outcome

    #try:
    #    return winners[u][c]
    #except KeyError:
    #    return "OOPS"
