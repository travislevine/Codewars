def accum(st):
    # Used to collect the results
    result_list = []

    for index, char in enumerate(st, start=1):
        # Multiply each char by index a * 1, b * 2 ... etc.
        segment = char * index
        
        #Format and append the case of the first character of each segment
        result_list.append(segment.capitalize())

    #Returns a string from the list
    return "-".join(result_list)
print(accum('abc'))


#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
#You have passed all of the tests! :)