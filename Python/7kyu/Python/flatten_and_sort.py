def flatten_and_sort(array):
    flatten = []
    # Loop through each sublist / row
    for row in array:
        # Loop through each number in the sublist / row and take the minimum value (to effectively sort)
        for num in row:
            flatten.append(num)
    return sorted(flatten)
print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

#You have passed all of the tests! :)
#https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python