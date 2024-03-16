def findMaxLength(nums):
    count = 0
    maxCount = 0
    countIndexMap = {0:-1}

    for i, num in enumerate(nums):
        if num == 1:
            count += 1
        else:
            count -= 1

        if count in countIndexMap:
            maxCount = max(maxCount, i - countIndexMap[count])
        else:
            countIndexMap[count] = i

    return maxCount

    # index = 0
    # maxCount = 0
    # count = 0
    # while index < len(nums):
    #     if nums[index] == 0 or nums[index] == 1:
    #         count += 1
    #     else:
    #         maxCount = max(maxCount, count)
    #         count = 0
    #     index += 1
    # maxCount = max(count, maxCount)

    # return maxCount

print(findMaxLength([0,1,2,0,0,1]))