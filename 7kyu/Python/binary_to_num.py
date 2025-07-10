def binary_array_to_number(arr):
  result_str = ""
  # This loop builds the complete binary string
  for num in arr:
    result_str += str(num)

  # Now, after the loop is done, convert the full string
  decimal_value = int(result_str, 2)
  return decimal_value

#https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python
#You have passed all of the tests! :)