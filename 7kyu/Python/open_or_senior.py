def open_or_senior(data):
    result = []
    for person in data: 
        if person[0] >= 55 and person[1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python