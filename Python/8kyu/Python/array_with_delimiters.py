def print_array(arr):
    return ",".join(str(x) for x in arr)

#You have passed all of the tests! :)

#If you expect nested arrays or objects and want consistency, use:
import json

def array_to_string(arr):
    return ",".join(json.dumps(x) for x in arr)
