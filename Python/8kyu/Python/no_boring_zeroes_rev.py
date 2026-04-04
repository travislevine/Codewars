def no_boring_zeros(n):
    # your code
    if n == 0:
        return n
    while n % 10 == 0:
        n //= 10
    return n
#https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/python
#You have passed all of the tests! :)