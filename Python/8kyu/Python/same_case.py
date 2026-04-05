def same_case(a, b):
    # 1. Guard Clause: If either is not a letter, return -1 immediately
    if not a.isalpha() or not b.isalpha():
        return -1
    
    # 2. Comparison: Check if their lowercase status matches.
    # If both are True (lower) or both are False (meaning both are upper), 
    # then they are the same case.
    if a.islower() == b.islower():
        return 1
    
    # 3. Fallback: They are both letters but failed the 'same case' check.
    return 0
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python