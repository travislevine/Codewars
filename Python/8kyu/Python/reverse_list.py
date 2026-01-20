def reverse_list(l):
    'return a list with the reverse order of l'
    some_empty = []
    for i in range(-1, (-len(l) - 1), -1):
        some_empty.append(l[i])
    return some_empty

print(reverse_list([1,2,3,4]))
#You have passed all of the tests! :)
#https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/python