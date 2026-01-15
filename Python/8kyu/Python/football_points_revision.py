def points(games):
    points = 0
    split_games = []
    #iterate through games directly
    for game in games:
        split_games = game.split(":")
        x = split_games[0]
        y = split_games[1]
        if x > y:
            points += 3
        elif x < y:
            pass
        elif x == y:
            points += 1
    return points

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
