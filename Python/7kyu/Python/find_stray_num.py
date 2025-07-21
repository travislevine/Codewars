def stray(arr):
    num_counts = {}
    for num in arr:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    for key, value in num_counts.items():
        if value == 1:
            return key
#You have passed all of the tests! :)
#https://www.codewars.com/kata/57f609022f4d534f05000024/train/python