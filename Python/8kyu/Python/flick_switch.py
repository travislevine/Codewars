def flick_switch(lst):
    current_value = True
    result_list = []
    for element in lst:
        if element == "flick":
            current_value = not current_value 
            result_list.append(current_value)
        else:
            result_list.append(current_value)
    return result_list
#You have passed all of the tests! :)
#https://www.codewars.com/kata/64fbfe2618692c2018ebbddb/train/python