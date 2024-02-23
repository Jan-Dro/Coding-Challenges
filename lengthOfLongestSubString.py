# def lengthOfLongestSubstring(s):
#     charIndexMap = {}
#     maxLength = 0
#     left = 0
    
#     for right in range(len(s)):
#         if s[right] in charIndexMap:
#             left = max(left, charIndexMap[s[right]] + 1)

#         charIndexMap[s[right]] = right
        
#         maxLength = max(maxLength, right - left + 1)
    
#     return maxLength


# print(lengthOfLongestSubstring("abcabcbb"))



















# def lengthOfstring(s):
#     charIndex = {}
#     left = 0
#     maxLength = 0

#     for right in range(len(s)):
#         if s[right] in charIndex:
#             left = max(left, charIndex[s[right]] + 1)

#         charIndex[s[right]] = right
#         maxLength = max(maxLength, right - left + 1)
#     return maxLength


# print(lengthOfstring('abcabcbb'))













def lengthOfstring(s):
    hashmap = {}
    left = 0
    maxLength = 0

    for right in range(len(s)):
        if s[right] in hashmap:
            left = max(left, hashmap[s[right]] + 1)
        hashmap[s[right]] = right
        maxLength = max(maxLength, right - left + 1)
    return maxLength



print(lengthOfstring('abcabcbb'))
