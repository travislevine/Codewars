def points(games):
    totalPoints = 0
    # Set up a loop
    for score in games:
        #Extract and parse the scores
        currentMatch = score.split(":")
        x = currentMatch[0]
        y = currentMatch[1]

        if x > y:
            totalPoints += 3
        elif x == y:
            totalPoints += 1
        elif x < y:
            continue
    return totalPoints


#You have passed all of the tests! :)
#https://www.codewars.com/kata/5bb904724c47249b10000131/train/python
