def friend(x):
    #Code
    output = []
    for name in x:
        if len(name) == 4:
            output.append(name)
    return output
print(friend(["Peter", "Stephen", "Joe"]))
#You have passed all of the tests! :)