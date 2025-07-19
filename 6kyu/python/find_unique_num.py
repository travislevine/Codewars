def find_uniq(arr):
    # your code here

    #1: Identity the recurring number
    recurring_num = 0

    # Placeholder for unique num
    unique_num = 0

        # Recurring number found
    if (arr[0] == arr[1]): 
        recurring_num = arr[0]
    else:
        if (arr[2] == arr[0]):
            unique_num = arr[1]
            return unique_num
    
    for num in arr:
        if (num != recurring_num):
            unique_num = num
            return unique_num
#https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
#You have passed all of the tests! :)