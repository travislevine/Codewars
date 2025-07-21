from collections import Counter
def highest_rank(arr):
    # 1: Count freq of each num
    counts = Counter(arr)
    # 2: Loop through counts to find most freq num
    max_frequency = 0
    result = 0
