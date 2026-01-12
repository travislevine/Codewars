def points(games):
    totalPoints = 0

    scoresSplit = []
    x_and_y = []
    # Set up a loop
    for score in games:
        #Extract and parse the scores
        scoresSplit = score.split(":")
        for char in scoresSplit:
            x_or_y = int(char)
            x_and_y.append(x_or_y)
    for i in range(len(x_and_y) - 1):
        if x_and_y[i] > x_and_y[i + 1]:
            totalPoints += 3
        elif x_and_y[i] == x_and_y[i + 1]:
            totalPoints += 1
        elif x_and_y[i] < x_and_y[i + 1]:
            pass
    return totalPoints

print(points(["3:1", "4:2", "7:4"]))
