def removeDuplicates2(nums):
    start = len(nums) -1

    while start > 0:
        if len(nums) < 3:
            break
        if nums[start] == nums[start - 1] and nums[start] == nums[start - 2]:
            nums.pop(start)
        start-= 1

    k = len(nums)
    return k



print(removeDuplicates2([0,0,1,1,1,1,2,3,3]))