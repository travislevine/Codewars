def remove_exclamation_marks(s):
    #your code here
    working = []
    for char in s:
        if char != "!":
            working.append(char)
    return ''.join(working) 
#https://www.codewars.com/kata/57a0885cbb9944e24c00008e