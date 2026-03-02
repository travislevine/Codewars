def men_from_boys(arr):
    #your code here\

    return_list_even = []
    return_list_odd = []
    my_set = set(arr)
    for num in my_set:
        if num % 2 == 0:
            return_list_even.append(num)
        else:
            return_list_odd.append(num)
    return_list_even.sort()
    return_list_odd.sort(reverse=True)

    for odd in return_list_odd:
        return_list_even.append(odd)
    
    return return_list_even

#https://www.codewars.com/kata/5af15a37de4c7f223e00012d/train/python
#You have passed all of the tests! :)