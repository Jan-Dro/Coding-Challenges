
def firstMissingPos(nums):
    oneIsThere = False
    nums = sorted(nums)

    if 1 in nums:
        oneIsThere = True
    else:
        return 1
    
    currentNum = 0
    nextNum = 1
    while nextNum <= len(nums) - 1:
        if nums[currentNum] < 0:
            currentNum += 1
            nextNum += 1
        if nums[currentNum] + 1 == nums[nextNum]:
            currentNum += 1
            nextNum += 1
        else:
           return  nums[currentNum] + 1
    return nums[len(nums) - 1] + 1


    



print(firstMissingPos([1,2,0]))
print(firstMissingPos([3,4,-1,1]))
print(firstMissingPos([7,8,9,11,12]))