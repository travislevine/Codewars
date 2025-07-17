def find_deleted_number(arr, mixed_arr):
    #Your code here

    start_arr_sum = 0
    #1: Find the sum of start arr
    for num in arr:
        start_arr_sum += num

    second_arr_sum = 0
    #2: Find the sum of the mixed_arr
    for num in mixed_arr:
        second_arr_sum += num
    
    #3: Find the difference = start - mixed
    return start_arr_sum - second_arr_sum
#https://www.codewars.com/kata/595aa94353e43a8746000120/train/python
#You have passed all of the tests! :)