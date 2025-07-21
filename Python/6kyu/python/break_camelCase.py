def solution(s):
    result_string = ""
    for char in s:
        if char.isupper():
            result_string += " "
        result_string += char
    return result_string
print(solution("identifier"))

#https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
#You have passed all of the tests! :)