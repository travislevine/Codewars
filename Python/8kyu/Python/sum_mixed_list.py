def sum_mix(arr):
    total = 0
    for i in arr:
        if isinstance(i, str):
            total += int(i)
        else:
            total += i
    return total

#You have passed all of the tests! :)