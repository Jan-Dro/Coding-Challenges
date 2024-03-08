def searchInsert(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = (end + start) // 2

        if nums[middle] == target:
            return middle
        elif target > nums[middle]:
            start = middle + 1
        else:
            end = middle - 1

    return start


print(searchInsert([1,3,5,6], 5))