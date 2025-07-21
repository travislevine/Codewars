def even_numbers(arr,n):
    # Result even nums
    even_nums = []

    #1: Find all even numbers
    for even_num in arr:
        if even_num % 2 == 0:
            even_nums.append(even_num)
    
    # Select the last n numbers from even_nums using list slice
    final_nums = even_nums[-n:]
    return final_nums
#https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/train/python
#You have passed all of the tests! :)