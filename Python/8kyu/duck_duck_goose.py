def duck_duck_goose(players, position):
    # Calculate the index using modulo to handle wrap-around
    # (position - 1) converts 1-based input to 0-based index
    index = (position - 1) % len(players)
    
    # Return the name property of the player at that index
    return players[index].name
#https://www.codewars.com/kata/582e0e592029ea10530009ce/train/python
#You have passed all of the tests! :)