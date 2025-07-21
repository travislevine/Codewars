def div_con(x):
    # your code here
    non_string_ints = 0

    # Keep track of string integers
    string_ints = 0

    # Equation non_string_ints - string_ints
    result_num = 0

    # Loop through the mixed list
    for num in x:
        if isinstance(num, int):
            non_string_ints += num
        else:
            string_ints += int(num)

    result_num = non_string_ints - string_ints
    return result_num
#https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python
#You have passed all of the tests! :)