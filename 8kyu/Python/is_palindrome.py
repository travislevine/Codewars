def is_palindrome(s):
    #convert the string to lowercase
    s = s.lower()

    #Reverse the string and compare
    return s == s[::-1]

print(is_palindrome("madam"))      # True
print(is_palindrome("RaceCar"))    # True
print(is_palindrome("hello"))      # False

#https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python