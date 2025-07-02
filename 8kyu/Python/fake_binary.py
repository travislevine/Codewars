def fake_bin(x):
    result = []
    int(x)
    for num in x:
        if num < 5:
            result.append(0)
        elif num > 5:
            result.append(1)
    return str(result)
#https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python
#You have passed all of the tests! :)