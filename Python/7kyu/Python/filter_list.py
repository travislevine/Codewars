def filter_list(arr):
    'return a new list with the strings filtered out'
    result = []
    for item in arr:
        if type(item) is int:
            result.append(item)
    return result
print(filter_list(['1', 2, '3', 'four', 5])) # Should return [2, 5]
#You have passed all of the tests! :)
#https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python