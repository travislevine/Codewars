def distinct(seq):
    result = []
    for i in seq:
        if i not in result:
            result.append(i)
    return result
#You have passed all of the tests! :)
#https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python