def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    high = max(nums)
    low = min(nums)
    return f"{high} {low}"
#You have passed all of the tests! :)
#https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python