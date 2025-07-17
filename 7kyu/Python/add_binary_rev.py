def add_binary(a,b):
    #your code here
    
    #1: Add the a + b to get the sum
    working_sum = a + b

    # 2: Convert the working some to binary
    binary_num = bin(working_sum)

    # 3: Convert the binary to a str, slice and return
    return str(binary_num[2:])
