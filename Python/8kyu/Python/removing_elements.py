def remove_every_other(my_list):
    result = []
    for i in (range(len(my_list))):
        if i % 2 == 0:
            result.append(my_list[i])
    return result
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python