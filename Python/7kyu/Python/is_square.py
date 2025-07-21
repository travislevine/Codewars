def is_square(n):    
    if n < 0:
        return False
    square_root = n ** 0.5 # Calculates the square root of n

    # Check if square root is a whole number, if yes, return True
    return square_root % 1 == 0
#https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
#You have passed all of the tests! :)