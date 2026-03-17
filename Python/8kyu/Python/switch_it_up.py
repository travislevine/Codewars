def switch_it_up(number):
    number_map = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    # .get() prevents an error if a number outside 0-9 is entered
    return number_map.get(number, "Invalid number")
#https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python
#You have passed all of the tests! :)