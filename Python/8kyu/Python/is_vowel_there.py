def is_vow(inp):
    for i in range(len(inp)):
        if inp[i] in [97, 101, 105, 111, 117]:
            inp[i] = chr(inp[i])
    return inp
#You have passed all of the tests! :)
#https://www.codewars.com/kata/57cff961eca260b71900008f/train/python