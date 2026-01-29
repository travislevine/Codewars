def problem(a):
    # First, check if 'a' is a string
    if isinstance(a, str):
        return "Error"
    
    # Multiply by 50, then add 6
    # Python follows PEMDAS, so multiplication happens before addition
    return (a * 50) + 6
#You have passed all of the tests! :)