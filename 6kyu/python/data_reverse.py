def data_reverse(data):
    chunks = []
    for i in range(0, len(data), 8):
        chunk = data[i:i+8]
        chunks.append(chunk)
    # 2: Reverse the order of the chunks
    reversed_chunks = chunks[::-1]
    # 3:  Flatten list
    flat_list = []
    for chunk in reversed_chunks:
        flat_list.extend(chunk)
    return flat_list
print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
#https://www.codewars.com/kata/569d488d61b812a0f7000015/train/python
#You have passed all of the tests! :)