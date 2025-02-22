def get_size(w,h,d):
    #your code here
    area = 2 * (w * h + h * d + w * d)
    volume = w * h * d
    return [area, volume]
#You have passed all of the tests! :)