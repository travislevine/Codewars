def sort_array(source_array):
    odd_nums = []
    for num in source_array:
        if num % 2 != 0:
            odd_nums.append(num)
    sorted_odds = sorted(odd_nums)
    
    result = [] 
    odd_index = 0
    for item in source_array:
        if item % 2 != 0:
            result.append(sorted_odds[odd_index])
            odd_index += 1
        else:
            result.append(item)
    return result

print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python