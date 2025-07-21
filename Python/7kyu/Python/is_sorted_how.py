def is_sorted_and_how(arr):
    # your code here

    #Check for ascending order
    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr, reverse=True):
        return "yes, descending"
    else:
        return "no"
#https://www.codewars.com/kata/580a4734d6df748060000045/train/python
#You have passed all of the tests! :)