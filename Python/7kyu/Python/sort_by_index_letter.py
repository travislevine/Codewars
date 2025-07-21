#Python version of problem (verified by Gemini Pro)
def sort_by_index_letter(a1, a2):
    ...
    # 1: Prepare result list
    result_list = []

    #2: Loop through key array (a1)
    for i in range(len(a1)):
        #3: Loop through a2 to compare with a1
        for j in range(len(a2)):
            # Perform check: compare i to j
            if a1[i][0] == a2[j][0]:
                result_list.append(a2[j])
    return result_list
            
print(sort_by_index_letter(['giraffe', 'orangutan', 'impala', 'elephant', 'rhino'], ['rattlesnake', 'eagle', 'geko', 'iguana', 'octopus']))
#Return ['geko', 'octopus', 'iguana', 'eagle', 'rattlesnake']

#JavaScript version (does the same thing)
# function sortArray(a1, a2) {
#   // 1: Prepare result list (in JS, we declare arrays with let or const)
#   let resultList = [];

#   // 2: Loop through the key array (a1)
#   // The classic for loop in JS is very similar to Python's range(len(...))
#   for (let i = 0; i < a1.length; i++) {
#     // 3: Loop through a2 to compare with a1
#     for (let j = 0; j < a2.length; j++) {
#       // 4: Perform check: compare the first character of each string.
#       // In JS, you can get a character by its index, just like in Python.
#       // It's best practice to use `===` for strict comparison.
#       if (a1[i][0] === a2[j][0]) {
#         // In JS, we use .push() to append an item to an array.
#         resultList.push(a2[j]);
#       }
#     }
#   }
#   return resultList;
# }