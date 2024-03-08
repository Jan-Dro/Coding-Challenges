
def frequency(nums):
    numDict = {}
    for num in nums:
        if num in numDict:
            numDict[num] += 1
        else:
            numDict[num] = 1

    maxNum = max(numDict.values())
    count = 0
    for num in numDict.values():
        if num == maxNum:
            count += num

    return count


print(frequency([1,2,3,4,5]))