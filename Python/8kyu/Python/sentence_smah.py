def smash(words):
    # Sentence we are working with to return
    sentence = ""
    #Loop through the words list
    for word in words:
        sentence += word + " "
    return sentence.strip()
    #https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python
    #You have passed all of the tests! :)