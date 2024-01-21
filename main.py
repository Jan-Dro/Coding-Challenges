# def productExceptSelf(nums):
#     res = [1] * (len(nums))
#     # print(res)

#     prefix = 1
#     for i in range(len(nums)):
#         res[i] = prefix
#         print(res[i], res)
#         prefix *= nums[i]
#         print('--------')
#         # print(prefix)
#     postfix = 1
#     for i in range(len(nums) -1, -1, -1):
#         res[i] *= postfix
#         postfix *= nums[i]
#     return res    

# print(productExceptSelf([1,2,3,4]))


def maxSubArray(nums):
    maxSub = nums[0]
    currentSum = 0

    for number in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += number
        maxSub = max(maxSub, currentSum)
    return maxSub


print(maxSubArray([5,4,-1,7,8]))