def capitals(word):
    #your code here

    #Result list to store indices of uppercase words
    result_list = []

    # Track indices
    char_index = 0
    # Go through each character and check if the word is uppercase
    for i in word:
        if i.isupper():
            result_list.append(char_index)
        char_index += 1
    
#https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python
#You have passed all of the tests! :)