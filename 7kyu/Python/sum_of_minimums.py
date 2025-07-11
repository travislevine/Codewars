def sum_of_minimums(numbers):
    # 1: Keep track of total sum
    total_sum = 0
    min_val = 0

    for n in numbers:
        min_val = min(n)
        total_sum += min_val
    return total_sum
#https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python
#You have passed all of the tests! :)