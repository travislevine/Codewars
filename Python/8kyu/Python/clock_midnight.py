def past(h, m, s):
    # Good Luck!
    # Conversion factors
    min_in_hour = 60
    sec_in_min = 60
    mili_in_sec = 1000

    #Hours to seconds
    hr_seconds = h * min_in_hour * sec_in_min

    #Minutes to seconds
    min_seconds = m * sec_in_min

    # Combine all seconds
    total_seconds = hr_seconds + min_seconds + s

    #Convert to miliseconds
    total_seconds = total_seconds * 1000

    return total_seconds
#https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python
#You have passed all of the tests! :)