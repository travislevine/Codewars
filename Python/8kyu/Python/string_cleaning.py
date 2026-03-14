def string_clean(s):
    """
    Function will return the cleaned string
    """
    # Your code here
    working_str = ""
    for char in s:
        if char.isdigit():
            continue
        else:
            working_str += char
    return working_str
#You have passed all of the tests! :)
#https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/python