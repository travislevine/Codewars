def cannons_ready(gunners):
    for value in gunners.values(): # Looping through each value in the dicitonary
        if value != "aye": #If the current value is not equal to the str aye, break out the loop with a return statement
            return 'Shiver me timbers!'
    return "Fire!" #If all the values are equal to 'aye' the 'cannons' fire           