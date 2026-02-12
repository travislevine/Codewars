def solution(number):
    total_sum = 0
    if number < 0:
        return 0
    # check 'up to' input number
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum
#You have passed all of the tests! :)
#https://www.codewars.com/kata/514b92a657cdc65150000006/train/python