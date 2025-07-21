def is_vow(inp):
    temp = []
    for i in range(len(inp)):
        if inp[i] in [97, 101, 105, 111, 117]:
           element = chr(inp[i])
           temp.append(element) 
    return temp
print(is_vow([100, 100, 116, 105, 117, 121]))
