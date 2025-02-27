def rps(p1, p2):
    rules = {
        "rock": {"rock": "Draw!", "paper": "Player 2 won!", "scissors": "Player 1 won!"},
        "paper": {"rock": "Player 1 won!", "paper": "Draw!", "scissors": "Player 2 won!"},
        "scissors": {"rock": "Player 2 won!", "paper": "Player 1 won!", "scissors": "Draw!"},
    }
    return rules[p1][p2]

print(rps("rock", "paper"))
#You have passed all of the tests! :)

#Alternative solution
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"