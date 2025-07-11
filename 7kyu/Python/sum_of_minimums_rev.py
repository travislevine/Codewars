def sum_of_minimums(numbers):
    #Tracks the sum of all the minimums from each row added together
    total_min_sum = 0

    #Sort the 2D list in ascending order (not a necessary step for this problem)
    #sorted_nums = sorted(numbers)
    
    # Loop through sorted_nums list, count each min value
    for arr in numbers:
        #Finds the min of the sublist
        min_num = min(arr)
        total_min_sum += min_num
    return total_min_sum
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python