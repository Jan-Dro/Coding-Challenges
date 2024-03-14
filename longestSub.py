def longestSub(s):
    maxChars = s[0]
    count = 1
    left = 0
    right = 1
    maxCount = count
    while right < len(s):
        if s[right] not in maxChars:
            maxChars += s[right]
            count += 1
            right += 1
            maxCount = max(count, maxCount)
        else:
            left += 1
            right = left + 1
            maxChars = s[left]
            count = 1
    return maxCount


print(longestSub('bbbbb'))