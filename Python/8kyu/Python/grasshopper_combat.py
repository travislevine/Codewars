def combat(health, damage):
    #your code here
    health -= damage
    if health > 0:
        return health
    else:
        return 0
#You have passed all of the tests! :)
#https://www.codewars.com/kata/586c1cf4b98de0399300001d/train/python