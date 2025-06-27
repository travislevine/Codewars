def number(bus_stops):
    # Count ppl on bus
    passengers_on_bus = 0
    for i in range(len(bus_stops)):
        current_stop = bus_stops[i]

        people_on = current_stop[0]
        people_off = current_stop[1]

        passengers_on_bus += people_on
        passengers_on_bus -= people_off
    return passengers_on_bus
number(bus_stops = [[10, 0], [3, 5], [5, 8]])
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python