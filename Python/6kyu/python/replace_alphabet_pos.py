def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    postions = ""
    for char in text:
        if char.isalpha():
            postions += str(alphabet.index(char.lower()) + 1)  + " "
        else:
            continue
    return postions.strip()

    
print(alphabet_position("The sunset sets at twelve o' clock."))
#https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
#You have passed all of the tests! :)