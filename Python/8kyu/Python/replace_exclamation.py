def replace_exclamation(st):
    vowels = "aeiouAEIOU"
    new_st = ""
    for char in st:
        if char in vowels:
            new_st += "!"
        else:
            new_st += char
    return new_st
#You have passed all of the tests! :)
#https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/train/python