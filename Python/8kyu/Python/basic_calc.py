def calculate(num1, operation, num2): 
    # your code here
    valid_chars = ["+", "-", "*", "/"]
    if operation not in valid_chars:
        return None
    else:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num1 == 0 or num2 == 0:
                return None
            else:
                return num1 / num2
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5296455e4fe0cdf2e000059f/train/python