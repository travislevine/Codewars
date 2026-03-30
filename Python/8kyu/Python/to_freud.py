def to_freud(sentence):
  #your code here
  if sentence == "" or sentence == None:
     return ""
  words = sentence.split()
  freud = []
  for word in words:
    freud.append("sex")
  
  return " ".join(freud)
print(to_freud("test test"))
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5713bc89c82eff33c60009f7/train/python