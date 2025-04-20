import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    # Calculating sqrt of sq
    sqrt_result = math.sqrt(sq)

    #Check if square root is a whole number
    if sqrt_result % 1 == 0:
        #Apparently gives the root of the next perfect square
        sqrt_result += 1
        next_perfect_square = sqrt_result * sqrt_result
        return next_perfect_square
    return -1

print(find_next_square(100))