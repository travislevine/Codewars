def check(seq, elem):
    for item in seq:
        if item == elem:
            return True
    return False

print(check([4, 5, 6, 6], 7))

#You have passed all of the tests! :)