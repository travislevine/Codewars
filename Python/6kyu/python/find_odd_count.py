def find_it(seq):
    # Create an empty dictionary to store the counts
    dic = {}
    for num in seq:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    for count in dic:
        if dic[count] % 2 != 0:
            return count
print(find_it([1, 2, 2, 3, 3]))
#https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
#You have passed all of the tests! :)