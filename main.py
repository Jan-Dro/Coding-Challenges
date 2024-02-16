def mergeIntervels(nums):
    if not nums:
        return []
    
    nums.sort(key=lambda x: x[0])

    index = 0

    while index < len(nums) - 1:
        if nums[index][1] >= nums[index + 1][0]:
            nums[index][1] = max(nums[index][1], nums[index + 1][1])
            del nums[index + 1]
        else:
            index+= 1

    return nums


print(mergeIntervels([[1,3], [2,6], [8,10], [15,18]]))
