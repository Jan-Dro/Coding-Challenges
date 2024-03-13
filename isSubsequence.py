def isSubsequence(str1, str2):
    first = 0
    second = 0
    
    if str1 == str2:
        return True
    else:
       while first < len(str1) and second < len(str2):
            if str1[first] == str2[second]:
                first += 1
            second += 1
    return first == len(str1)
            

    

print(isSubsequence('twn', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn'))