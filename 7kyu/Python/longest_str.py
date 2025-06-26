def longest(a1, a2):
    # your code
    a3 = a1 + a2
    unique_alphabet_set = sorted(set(a3))
    unique_str = "".join(unique_alphabet_set)
    return unique_str
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python