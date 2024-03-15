
# def reorgStr(s):
#     newStr = []
#     start = 0
#     second = 1
#     lastChar = ''
#     while start < len(s) - 1:
#         if start == 0:
#             lastChar == s[start]
#             newStr.append(s[start])
#             start +=1
#             second += 1
#         elif 

#     return newStr


# print(reorgStr('aab'))
from collections import Counter
import heapq
from collections import Counter

def reorg(s):
    char_counts = Counter(s)
    sorted_chars = sorted(char_counts, key=lambda x: -char_counts[x])
    stack = []
    while sorted_chars:
        for i in range(len(sorted_chars)):
            if not stack or stack[-1] != sorted_chars[i]:
                stack.append(sorted_chars[i])
                char_counts[sorted_chars[i]] -= 1
                if char_counts[sorted_chars[i]] == 0:
                    sorted_chars.pop(i)
                break
        else:
            return ''
        
    return ''.join(stack)

print(reorg('aaab'))