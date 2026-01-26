def bmi(weight, height):
    #your code here
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
#You have passed all of the tests! :)
#https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python