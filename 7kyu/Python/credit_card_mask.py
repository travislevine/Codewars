# Revise this solution and understand the string slicing bit
def maskify(cc):
    str_length = len(cc)
    if str_length <= 4:
        return cc
    else:
        unmasked_part = cc[-4:]
        number_of_hashes = len(cc) - 4 #Revise this solution and understand the string slicing bit
        masked_part = '#' * number_of_hashes
        result = masked_part + unmasked_part
        return result
    #You have passed all of the tests! :)
    #https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python