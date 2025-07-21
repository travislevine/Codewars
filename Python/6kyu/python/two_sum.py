def two_sum(numbers, target):
    # Result list - score
    score = []
    # 1: Outer loop (looping through all elements)
    for i in range(len(numbers)):
        # 2: Inner Loop pick second number to add to first
        for j in range(i + 1, len(numbers)):
                    if numbers[i] + numbers[j] == target:
                           return (i, j)

#https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
#You have passed all of the tests! :)