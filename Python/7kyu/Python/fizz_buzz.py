def fizzbuzz(n):
    buzz_result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            buzz_result.append("FizzBuzz")
        elif i % 3 == 0:
            buzz_result.append("Fizz")
        elif i % 5 == 0:
            buzz_result.append("Buzz")
        else:
            buzz_result.append(i)
    return buzz_result
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5300901726d12b80e8000498/train/python