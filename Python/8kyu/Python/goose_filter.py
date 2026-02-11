geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    working_list = []
    #your code here
    for bird in birds:
        if bird not in geese:
            working_list.append(bird)
    return working_list
#You have passed all of the tests! :)
#https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python