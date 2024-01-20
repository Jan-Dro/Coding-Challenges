def containsDuplicate(nums):
    numDict = {}

    for num in nums:
        if num in numDict:
            return True
        else:
            numDict[num] = num
    return False

print(containsDuplicate([1,2,3,1]))