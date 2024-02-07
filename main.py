def frequencySort(s):

    charCount = {}

    for char in s:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    charCountSorted = sorted(charCount.items(), key=lambda x: x[1], reverse=True)

    res = ''
    for count, char in charCountSorted:
        res += char * count

    return res


print(frequencySort("aaAddppp"))