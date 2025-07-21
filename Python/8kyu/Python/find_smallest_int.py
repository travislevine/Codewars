def find_smallest_int(arr):
    target = arr[0]
    # Code here
    for item in arr:
        if item < target:
            target = item
    return target
print(find_smallest_int([1, 5, -1, -500, 50]))
#You have passed all of the tests! :)      

#Alternative solution
def findSmallestInt(arr):
    min = arr[0]
    for item in arr:
        if min > item:
            min = item
    return min