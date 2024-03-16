
def prodOfArrayExceptSelf(nums):
    length = len(nums)
    result = [1]* length
    index = 1

    for i in range(length):
        result[i] = index
        index *= nums[i]
    nextNum = 1
    for i in range(length -1, -1, -1):
        result[i] *= nextNum
        nextNum *= nums[i]
    return result

print(prodOfArrayExceptSelf([1,2,3,4]))