def two_sort(array):
    # your code here
    sorted_list = sorted(array) # Sorts the strings alphabetically
    first_word = sorted_list[0] #Taking the first letter in the list
    reurn_word = '***'.join(first_word)
    return reurn_word
#You have passed all of the tests! :)
#https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python