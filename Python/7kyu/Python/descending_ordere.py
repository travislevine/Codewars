def descending_order(num):
    # Bust a move right here
    str_convert = str(num)
    sort_str = sorted(str_convert, reverse=True)
    result = int("".join(sort_str))
    return result

print(descending_order(42145))
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python