def findMin(nums):
    start = 0
    end = len(nums) - 1
    minimumNum = nums[0]

    while start <= end:
        minimumNum = min(minimumNum ,nums[start], nums[end])
        start += 1
        end -= 1
    return minimumNum

print(findMin([11,13,15,17]))


