def reverse_words(s):
    the_split = s.split()
    new_split = the_split[-1::-1]
    return " ".join(new_split)



#https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python
#You have passed all the tests :)