def findDuplicate(nums):
    # hash = {}
    # for num in nums:
    #     if num in hash:
    #         return num
    #     else:
    #         hash[num] = 0
    # return -1
    nums = sorted(nums)
    numNeighbor = 1
    currentNum = 0
    
    for i in range(len(nums) - 1):  
        if nums[currentNum] == nums[numNeighbor]:
            return nums[currentNum]
        numNeighbor += 1
        currentNum += 1
    
        
print(findDuplicate([1, 2, 3, 2, 4]))