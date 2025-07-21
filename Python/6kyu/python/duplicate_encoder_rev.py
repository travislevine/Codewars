def duplicate_encode(word):
    #your code here

    # Step 1: Standardize the string to all lowercase (convention)
    lower_word = word.lower()
    
    # Step 2: Create an empty dictionary to keep count of characters in the word
    counts = {}

    #Step 4: Create an empty list to store the string being built
    result_list = []

    #Step 3: Loop through lower_word and add char count to counts{}
    for char in lower_word:
        if char in counts:
            counts[char] += 1
        # If the char is not in counts, set it to 1
        else:
            counts[char] = 1

    #Step 5: Loop through the word again, this time checking dictionary to build the result_list
    for char in lower_word:
        if counts[char] > 1:
            result_list.append(")")
        else:
            result_list.append("(")
    
    # Step 6: using .join() to create the string to return
    final_result = ''.join(result_list)
    return final_result

print(duplicate_encode("recede"))
#You have passed all of the tests! :)
#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python