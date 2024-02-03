def searchInserted(nums, target):
    start = 0
    end = len(nums) - 1



    while start < len(nums) - 1:
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            start += 1
            end -= 1

    
    tempNums = nums
    tempNums.append(target)
    sortedNums = sorted(tempNums)
    index = sortedNums.index(target)
    return index

print(searchInserted([4,5,1,3], 3))