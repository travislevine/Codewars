def sum_two_smallest_numbers(numbers):
    #Sorting the numbers list in ascending order into a new list
    ascending_list = sorted(numbers)

    #Adding thw two smallest numbers together
    add_two_lowest = ascending_list[0] + ascending_list[1]
    ascending_list.append(add_two_lowest)
    
    return add_two_lowest
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453])) 
#You have passed all of the tests! :)
#https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python