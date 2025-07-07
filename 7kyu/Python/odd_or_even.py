def odd_or_even(arr):
    #Step 1: Create a sum variable
    arr_sum = 0

    # Step 2: Loop through arr and sum all its elements
    for num in arr:
        arr_sum += num

    # Step 3: Determine if the sum of elements is even
    if arr_sum % 2 == 0:
        return "even"
    else:
        return "odd"
    #You have passed all of the tests! :)
    #https://www.codewars.com/kata/5949481f86420f59480000e7/train/python