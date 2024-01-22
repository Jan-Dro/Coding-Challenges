def search(nums, target):
    start = 0
    end = len(nums) -1
    while start <= end:

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            start += 1
            end -= 1
    return -1


print(search([4,5,6,7,0,1,2], 3))