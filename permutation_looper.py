
def create_permutations(numpad_list):
    if len(numpad_list) == 0:
        return [[]]
    
    permutations = []

    for i in range(len(numpad_list)):
        currentElement = numpad_list[i]

        remaining_list = numpad_list[:i] + numpad_list[i+1:]
        for p in create_permutations(remaining_list):
            permutations.append([currentElement] + p)
    return permutations


print(create_permutations([1,2,3]))