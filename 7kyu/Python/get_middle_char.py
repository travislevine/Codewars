def get_middle(s):
    str_length = len(s)
    middle = str_length // 2

    if str_length % 2  == 0:
        return s[middle - 1: middle + 1] # Revise this line
    else: 
        return s[middle]
#You have passed all of the tests! :)
#https://www.codewars.com/kata/56747fd5cb988479af000028/train/python