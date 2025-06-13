def square_digits(num):
    # Your code here
    convert_str = str(num)
    result = ""
    for digit in convert_str: #For each digit
        sqr = int(digit) # Convert to an integer
        squared = sqr * sqr #Square the integer
        result += str(squared) # Convert the result to a string
    final_result = int(result)
    return final_result
#You have passed all of the tests! :)
#https://www.codewars.com/kata/546e2562b03326a88e000020/train/python