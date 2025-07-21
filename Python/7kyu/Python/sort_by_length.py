# Easy solution (pythonic ish)
def sort_by_length(arr):
    return sorted(arr, key=len)
#You have passed all of the tests! :)
#https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python

# More manual solution
# You have your array of strings: ["Telescopes", "Glasses", "Eyes", "Monocles"].

def sort_by_length_manual(arr):
    swapped = True #  Start with True to make sure the loop runs at least once
    while swapped:
        swapped = False  # Reset Flag Assume we won't swap anything in this new pass
        # First pass
        for i in range(len(arr) - 1):
            if len(arr[i]) > len(arr[i + 1]):
                # Perform the swap with a temp variable
                temp = arr[i]
                arr[i] = arr[i + 1] # Telescopes = Glasses
                arr[i + 1] = temp # Glasses = Telescoepes
                # Set the flag to True as we have done a swap
                swapped = True
    return arr