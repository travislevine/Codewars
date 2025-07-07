def create_phone_number(n):
    #your code here
    result_str = "("
    for i in range(len(n)):
        result_str += str(n[i]) 
        if i == 2:
            result_str += ") "
        if i == 5:
            result_str += "-"
    return result_str

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
#https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
#You have passed all of the tests! :)