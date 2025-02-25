def smallest_int(arr):
    target = arr[0] #Sets the target to the first element in the arr
    
    for item in arr: #Checking each element in arr
        if item < target: # pretend we have an arr [5, 4, 3]
            target = item
    return target

print(smallest_int([5, -1, 4, -400, 3, -1]))