def flatten_and_sort(array):
    # Final list to return once array has been flattened
    result_list = []

    #Loop through each row
    for row in array:
        # Loop through each value in sublist
        for num in row:
            result_list.append(num)
    return sorted(result_list)

#https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python
#You have passed all of the tests! :)