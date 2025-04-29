def arr_check(arr):
    for item in arr:
        if type(item) is not list:
            return False
        else:
            continue
    return True
#You have passed all of the tests! :)
#https://www.codewars.com/kata/582c81d982a0a65424000201/train/python