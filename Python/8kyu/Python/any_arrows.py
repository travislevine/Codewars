def any_arrows(arrows):
    # Check if any arrow is NOT damaged
    return any(not arrow.get('damaged', False) for arrow in arrows)
#You have passed all of the tests! :)
#https://www.codewars.com/kata/559f860f8c0d6c7784000119/train/python