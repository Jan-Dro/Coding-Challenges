# def longestCommonSubsequence(text1, text2):
#     numStorage = {}
#     count = 0

#     numList = list(text1)
#     text2 = list(text2)

#     for letter in text2:
#         if letter in numStorage:
#             count+= 1
#         else:
#             numStorage[letter] = letter
#     return count


# print(longestCommonSubsequence('abcde', 'ace'))


def longestCommonSubsequence(text1, text2):
    # list1 = list(text1)
    # list2 = list(text2)

    # biggestNumber = max(list1, list2, key=len)
    # # biggestNumber.sort()
    # biggestNumber = set(biggestNumber)
    # smallestList = min(list1, list2, key=len)
    # # smallestList.sort()
    # smallestList = set(smallestList)


    # print(smallestList, biggestNumber)


    # answer = biggestNumber.intersection(smallestList)

    # return answer

    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1) -1, -1, -1):
        for j in range(len(text2) -1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]

print(longestCommonSubsequence('ezupkr', 'ubmrapg'))
