def getSumAbsoluteDifferences(nums):
    if not 2 <= len(nums) <= 10**5:
        raise ValueError("Length of nums must be between 2 and 10^5")
    
    for i in range(len(nums) - 1):
        if not (1 <= nums[i] <= nums[i + 1] <= 10**4):
            raise ValueError("Elements in nums must be in non-decreasing order and between 1 and 10^4")
    newRes = []

    for i in range(len(nums)):
        currentNum = 0
        for j in range(len(nums)):
            if i == j:
                continue
            else:
                currentNum += abs(nums[j] - nums[i])
        newRes.append(currentNum)

    return newRes


print(getSumAbsoluteDifferences([1,4,6,8,10]))