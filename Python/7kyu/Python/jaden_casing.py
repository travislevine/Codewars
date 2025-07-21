def to_jaden_case(string):
    capitalized_words = []
    for item in string.split():
        capitalized_words.append(item.capitalize())
    return " ".join(capitalized_words)
print(to_jaden_case("testing, the words in a sentence"))
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python