# def isMatch(s, p):
#     isvalid = '*'
#     valid1 = '?'

#     if len(p) < 2:
#         if p == '?' or p == '*':
#             return True

#     validationChecker = True
#     for i, char in enumerate(s):
#         if char == p[i] or char == isvalid or char == valid1:
#             print(p[i])
#             continue
#         else:
#             return False
#     return validationChecker

# print(isMatch('aa', '*a'))




def majorityElement(nums):
    placeHolder = {}

    for number in nums:
        if number in placeHolder:
            placeHolder[number] += 1
        else:
            placeHolder[number] = 0

    maximum = max(placeHolder, key=placeHolder.get)
    return maximum
    

print(majorityElement([2,2,2,1,0,1]))