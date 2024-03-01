def majorityElement(nums):
    # numDict = {}

    # for num in nums:
    #     if num in numDict:
    #         numDict[num] += 1
    #     else:
    #         numDict[num] = 1

    # maxNum = max(numDict, key=lambda x:numDict[x])

    # return maxNum

    for num in nums:
        if nums.count(num) > len(nums) //2:
            return num

    

print(majorityElement([3,2,3]))
