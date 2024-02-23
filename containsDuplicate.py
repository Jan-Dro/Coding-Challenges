def containsDuplicate(nums):
    nums = sorted(nums)
    number = nums[0]
    nums.pop(0)

    for num in nums:
        if num == number:
            return True
        else:
            number = num
    return False
        

print(containsDuplicate([1,2,2,3]))