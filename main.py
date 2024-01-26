def anagram(str1, str2):
    sortedStr1 = ''.join(sorted(str1))
    sorted2 = ''.join(sorted(str2))


    if sortedStr1 == sorted2:
        return True
    return False


print(anagram('anagram','nagaram'))