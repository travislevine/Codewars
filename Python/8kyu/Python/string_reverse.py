def reverse(st):
    split_temp = []
    reversed = []
    # Your Code Here
    split_temp = st.split(" ")
    new_string = split_temp[1] + " " + split_temp[0]
    return new_string

print(reverse("hello world"))
#You have passed all of the tests! :)
#https://www.codewars.com/kata/57a55c8b72292d057b000594/train/python