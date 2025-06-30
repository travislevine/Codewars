def array_diff(a, b):
    result = []
    for num in a:
        if num not in b:
            result.append(num)
    return result

#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
#You have passed all of the tests! :)