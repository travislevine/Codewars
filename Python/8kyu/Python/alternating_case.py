def to_alternating_case(string):
    new_str = ""
    for char in string:
        if char == char.upper():
            new_str += char.lower()
        else:
            new_str += char.upper()
    return new_str
#https://www.codewars.com/kata/56efc695740d30f963000557/train/python
#You have passed all of the tests! :)