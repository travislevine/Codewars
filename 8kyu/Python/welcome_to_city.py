def say_hello(name, city, state):
    result_string = ' '.join(name)
    return f"Hello, {result_string}! Welcome to {city}, {state}!"
    
print(say_hello(['John', 'Smith'], "Phoenix", "Arizona"))
#You have passed all of the tests! :)