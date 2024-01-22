# def threeSum(nums):
#     nums.sort()
#     result = []

#     for i in range(len(nums) - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         start, end = i + 1, len(nums) - 1

#         while start < end:
#             total = nums[i] + nums[start] + nums[end]

#             if total == 0:
#                 result.append([nums[i], nums[start], nums[end]])
                
#                 while start < end and nums[start] == nums[start + 1]:
#                     start += 1
#                 while start < end and nums[end] == nums[end - 1]:
#                     end -= 1
#                 start += 1
#                 end -= 1
#             elif total < 0:
#                 start += 1
#             else:
#                 end -= 1
#     return result 

# print(threeSum([-1,0,1,2,-1,-4]))




def threeSum(nums):
    ans = []
    nums.sort()

    for i, number in enumerate(nums):
        if i > 0 and number == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            threeSum = number + nums[left] + nums[right]
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                ans.append([number, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return ans

print(threeSum([-1,0,1,2,-1,-4]))

