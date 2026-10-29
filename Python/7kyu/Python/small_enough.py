def small_enough(array, limit):
    for item in array:
        if item > limit:
            return False
    return True
#You have passed all of the tests! :)
#https://www.codewars.com/kata/57cc981a58da9e302a000214/train/python
  