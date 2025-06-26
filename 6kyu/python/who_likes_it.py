def likes(names):
    num_names = len(names) # Gets the numbers of names in names
    if num_names == 0:
        return "no one likes this"
    elif num_names == 1:
        return f"{names[0]} likes this"
    elif num_names == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num_names == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {num_names - 2} others like this"
print(likes(["Josh", "Peter", "John", "Max", "Alice"]))
#https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
#You have passed all of the tests! :)