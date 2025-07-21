def order(sentence):
  # code here
  if sentence == "" or sentence == None:
    return ""
  words = sentence.split()
  result = sorted(words, key=lambda word: int([char for char in word if char.isdigit()][0]))
  return ' '.join(result)
print(order("is2 Thi1s T4est 3a"))
#https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
#You have passed all of the tests! :)