def positive_sum(arr):
    # Your code here
    result_arr = []
    total = 0
    for num in arr:
        if num > 0:            
            result_arr.append(num)
    
    for num in result_arr:
        total += num
    return total
#https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
#You have passed all of the tests! :)