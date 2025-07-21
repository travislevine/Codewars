def correct(s):
    corrected_list = []
    for char in s:
        if char == "5":
            corrected_list.append("S")
        elif char == "0":
            corrected_list.append("O")
        elif char == "1":
            corrected_list.append("I")
        else:
            corrected_list.append(char)
    final_string = "".join(corrected_list)
    return final_string
print(correct('L0ND0N'))
#You have passed all of the tests! :)
#https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/python