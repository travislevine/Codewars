def digitize(n):
    temp_str = str(n)
    work_list = []
    for i in range (len(temp_str) - 1, -1, -1):
        work_list.append(int(temp_str[i]))
    return work_list

print(digitize(0))