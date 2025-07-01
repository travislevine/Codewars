def remove_smallest(numbers):
    # Edge case first - handle empty list
    if numbers == []:
        return []
    
    # Find the smallest value to remove
    smallest_value = min(numbers)

    # Create a copied list - do not mutate the original list
    copied_list = numbers.copy()

    # Remove the smallest value from the copied list
    copied_list.remove(smallest_value)

    # Return the copied_list
    return copied_list
#https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
#You have passed all of the tests! :)