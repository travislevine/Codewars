def xo(s):
    #standardize the input
    s = s.lower()

    # Get counts
    x_count = s.count('x')
    o_count = s.count('o')

    # Compare counts
    if x_count == o_count:
        return True
    else:
        return False
#https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
#You have passed all of the tests! :)