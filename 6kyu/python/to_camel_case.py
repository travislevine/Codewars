def to_camel_case(text):
    replaced_text = text.replace("-", "_")
    
    split_list = replaced_text.split("_")
    
    # Handle empty input case
    if not split_list or split_list == ['']:
        return ""

    # Store the first word as it follows a different casing
    first_word = split_list[0]

    # Take the remaining words and store them in a different list
    remaining_words = split_list[1:]

    # Captialized words
    capitalized_words = []

    # Every word that followed a delimeter must be capitalized
    for word in remaining_words:
        capitalized_words.append(word.capitalize())

    # Rejoin everything
    return first_word + "".join(capitalized_words)

print(to_camel_case("the_Stealth-Warrior"))
#https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
#You have passed all of the tests! :)