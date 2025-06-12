def count_sheep(n):
    # your code
    result = ""
    if n == 0:
        return ""
    for i in range(1, n + 1):
        result += f"{i} sheep..."
    return result
print(count_sheep(5))
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python