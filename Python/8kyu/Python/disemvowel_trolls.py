def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for item in string_:
        if item not in vowels:
            result += item
    return(result)
print(disemvowel("peter is lovely"))
#You have passed all of the tests! :)