def sort_by_index_letter(a1, a2):
    # Start with the result list we return
    result_list = []

    # We need to first loop through a1 by the index
    for i in range(len(a1)):
        # We now need to loop through a2 and check its values against a1
        for j in range(len(a2)):
            # If the first letter of the first word in a1 matches the same in a2, append a2[j]
            if a1[i][0] == a2[j][0]:
                result_list.append(a2[j])
    # Return the sorted list
    return result_list