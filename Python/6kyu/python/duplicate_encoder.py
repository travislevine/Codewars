def duplicate_encode(word):
    #Create a new version of the input string that is entirely lowercase.
    word_lower = word.lower()

    # Keep count of word frequency with dict
    counts = {}

    # Result list to store the new string
    result_list = []

    # Looping through the input str to count and add word occurrences to dictionary
    for char in word_lower:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    # Loop through the input str to add items to result_list
    for char in word_lower:
        if counts[char] > 1:
            result_list.append(")")
        elif counts[char] == 1:
            result_list.append("(")
    return "".join(result_list)
#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
#You have passed all of the tests! :)