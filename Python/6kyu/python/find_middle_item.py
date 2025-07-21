def gimme(input_array):
    # Implement this function
    
    # 1: Sort the input_array (can be manual or python built in)
    sorted_inp_arr = sorted(input_array)

    #2: Find the middle value 
    middle_value = sorted_inp_arr[1]

    #3: Find original value index in input_array
    original_value = input_array.index(middle_value)

#https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python
#You have passed all of the tests! :)
