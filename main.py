def sortColors(nums):
    if not nums:
        return nums
    
    pivot = nums[0]
    less = [i for i in nums[1:] if i <= pivot]
    greater = [i for i in nums[1:] if i > pivot]

    return sortColors(less) + [pivot] + sortColors(greater)


print(sortColors([2,0,2,1,1,0]))