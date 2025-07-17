def find_deleted_number(arr, mixed_arr):
    #Your code here
    # Calculate the expected sum
    num_sum_arr_1 = 0
    for num in arr:
        num_sum_arr_1 += num

    #2: Calculate the actual sum of second arr
    num_sum_arr_2 = 0
    for num in mixed_arr:
        num_sum_arr_2 += num
    
    #3: Find the difference and return the sum
    difference = num_sum_arr_1 - num_sum_arr_2
    return difference
#https://www.codewars.com/kata/595aa94353e43a8746000120/train/python
# You have passed all of the tests! :)