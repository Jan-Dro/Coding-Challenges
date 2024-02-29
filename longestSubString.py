def longestSubString(s):
    charset = set()
    left = 0
    maxLength = 0
    joined = ''

    for right in range(len(s)):
        while s[right] in charset:
            charset.remove(s[left])
            left += 1
        charset.add(s[right])

        if(right - left +1 ) > maxLength:
            maxLength = right - left + 1
            longesSub = s[left:right + 1]

    return maxLength, longesSub



print(longestSubString('abcabcbb'))