def delete_nth(order,max_e):
    # 1: Create an empty list
    result = []

    # Create an empty dictionary to store each number as a key and current count as value
    counts = {}

    #2: Loop through input list
    for number in order:
        current_count = counts.get(number, 0)
        if current_count < max_e:
            result.append(number)
            counts[number] = current_count + 1
    return result

#https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
#You have passed all of the tests! :)