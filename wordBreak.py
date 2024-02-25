# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false



def wordBreak(s, wordDict):
    index = 0
    answer = ''
    for word in wordDict:
        for char in word:
            if s[index] == char:
                answer += char
                index += 1
    print(answer)


print(wordBreak('applepenapple', ["apple", 'pen']))