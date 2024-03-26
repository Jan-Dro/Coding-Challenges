def findDuplicateInArray(nums):
    numHash = {}
    res = []
    for num in nums:
        if num in numHash:
            res.append(num)    
        else:
            numHash[num] = 1


    return res

print(findDuplicateInArray([4,3,2,7]))