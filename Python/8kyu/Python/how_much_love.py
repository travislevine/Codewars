def how_much_i_love_you(nb_petals):
    # your code
    phrases = ["I love you", " a little", "a lot", "passionately", "madly", "not at all"]
    index = (nb_petals - 1) % 6
    return phrases[index]
#You have passed all of the tests! :)
#https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python