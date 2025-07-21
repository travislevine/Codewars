def string_ends_with(text, ending):
    # your code here...
    ending_length = len(ending) # Calculates the length of the ending string
    if ending_length == 0:
        return True
    
    # This is the corrected slice from the end of the string
    sliced = text[-ending_length:]

    if sliced == ending:
        return True
    else:
        return False
print(string_ends_with('ab', ''))
#You have passed all of the tests! :)
#https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
