def duplicate_count(text):
    # Your code goes here
    
    # Normalise the string
    txt_lower = text.lower()

    # Final counter variable to count duplicates
    duplicate_count = 0

    # Acts as a frequency counter for each char in txt_lower
    char_counts = {}
    
    # Loop through each character in txt_lower
    for char in txt_lower:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Loop through the values in teh char_counts to count duplicates
    for num in char_counts.values():
        if num > 1:
            duplicate_count += 1
    return duplicate_count
#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
#You have passed all of the tests! :)