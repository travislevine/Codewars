def invert(lst):
    inverted = []
    for num in lst:
        if num > 0:
            inverted.append(num * -1)
        else:
            inverted.append(num * -1)
    return inverted

print(invert([1,2,3,4,5]))
#https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
#You have passed all of the tests! :)