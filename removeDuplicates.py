def remove_duplicates(ids_list):
    ids_list = sorted(ids_list)
    i = len(ids_list) - 1
    while i > 0:
        if ids_list[i] == ids_list[i - 1]:
            ids_list.pop(i)
        i -= 1

    return [len(ids_list) ,ids_list]

print(remove_duplicates([1,1,1,2,2,2,3,3,3,4,4,5]))