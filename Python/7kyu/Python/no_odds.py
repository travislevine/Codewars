def no_odds(values):
    # Return list of only even values
    evens = []
    for num in values:
        if num % 2 == 0:
            evens.append(num)
    return evens
    #https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce/train/python
    #You have passed all of the tests! :)