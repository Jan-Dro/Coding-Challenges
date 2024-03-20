def firstMissingPos(nums):
    nums = sorted(nums)
    newList = []
    for num in nums:
        if num > 0:
            newList.append(num)
    currentNum = newList[0]
    if not newList or newList[0] > 1:
        return 1
    for nums in newList[1:]:
        if currentNum + 1 == nums:
            currentNum = num
        else:
            return currentNum + 1

    return newList[-1] + 1


print(firstMissingPos([2,0]))