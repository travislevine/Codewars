def remove_url_anchor(url):
    result_list = []
    for char in url:
        if char != "#":
            result_list.append(char)
        else:
            break
    return "".join(result_list)
#You have passed all of the tests! :)
#https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python