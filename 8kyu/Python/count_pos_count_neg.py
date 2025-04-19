def count_positives_sum_negatives(arr):
    if arr == None or arr == []:
        return []
    positive_count = 0
    negative_sum = 0
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_sum += num
    new_list = [positive_count, negative_sum]
    return new_list
#You have passed all of the tests! :)
#https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python