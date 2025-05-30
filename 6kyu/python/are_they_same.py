def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    elif len(array1) != len(array2):
        return False
    return sorted([x ** 2 for x in array1]) == sorted(array2)

#Alternative solution
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2) # It seems each element in array1 is squared and sorted
    except: #This except accounts for NULL arrays and if the array's lengths don't match
        return False 