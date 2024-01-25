
def longestSubString(s):
    start = 0
    end = 0

    numbDict = {}
    max_length = 0
    tempCount = 0

    while end < len(s):
        char = s[end]
        if char not in numbDict or numbDict[char] < start:
            numbDict[char] = end
            end += 1
            tempCount = max(tempCount, end - start)
        else:
            start = numbDict[char] + 1

    return max(tempCount, max_length)

print(longestSubString('pwwkew'))