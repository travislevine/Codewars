def number(lines):
    #your code here
    # Stores the final result of strings with numbers
    modified = []
    count = 0
    for line in lines:
        count += 1
        current_str = line
        apnd_str = f"{count}: {current_str}"
        modified.append(apnd_str)
    return modified

#You have passed all of the tests! :)
#https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python