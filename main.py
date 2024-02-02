# def armstrong(nums):
#     nums1 = list(str(nums))
#     testNum = len(nums1)
#     answer = 0

#     for num in nums1:
#         answer += (int(num) ** testNum)

#     if answer == int(nums):
#         return True
#     return False


# print(armstrong("371"))




# def longestPalindromeSeq(s):
    # characters = {}

    # if len(s) == 1:
    #     return 1

    # for char in s:
    #     if char in characters:
    #         characters[char] += 1
    #     else:
    #         characters[char] = 1

    # placeholder = []

    # for char in s:
    #     if characters[char] > 1:
    #         placeholder.append(char)
    
    # placeholder = ''.join(placeholder)
    # longest_palindrome = ""

    # for i in range(len(placeholder)):
    #     for j in range(i, len(placeholder)):
    #         substr = placeholder[i:j+1]
    #         if substr == substr[::-1] and len(substr) > len(longest_palindrome):
    #             longest_palindrome = substr

    # return len(longest_palindrome)

#     n = len(s)

#     if n <= 1:
#         return n
    
#     longest_length = 1

#     for i in range(n):
#         for j in range(i, n):
#             substr = s[i:j+1]
#             if substr == substr[::-1]:
#                 longest_length = max(longest_length, len(substr)) 
#     return longest_length

# print(longestPalindromeSeq('bbbab'))




# class BasicEmployee:
#     def __init__(self, name, employee_id, department):
#         self.name = name
#         self.employee_id = employee_id
#         self.department = department

# class Progammer(BasicEmployee):
#     def __init__(self, name, employee_id, department, languages):
#         super().__init__(name, employee_id, department)
#         self.language = languages



def longestPalindromeSeq(s):
    n = len(s)

    if n <= 1:
        return n
    
    longest_length = 1

    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if substr == substr[::-1]:
                longest_length = max(longest_length, len(substr)) 
    return longest_length

print(longestPalindromeSeq('bbbab'))