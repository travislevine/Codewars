def find_uniq(arr):
    # your code here
    # Step 1: Reliably find the normal number.
    if arr[0] == arr[1]:
        recurring_num = arr[0]
    else:
        # If the first two differ, the third is the tie-breaker.
        recurring_num = arr[2] # The normal number MUST be the third one in this case
    
    for num in arr:
        if (num != recurring_num):
            unique_num = num
            return unique_num
#https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
#You have passed all of the tests! :)