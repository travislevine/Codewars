from collections.abc import Callable

def _if(bool, func1: Callable, func2: Callable):
    if bool:
        func1()
    else:
        func2()
#You have passed all of the tests! :)
#https://www.codewars.com/kata/54147087d5c2ebe4f1000805/train/python