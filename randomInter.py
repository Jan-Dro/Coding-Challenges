def increment(nums, digit):
    missing_nums = []
    theNum = nums[0]
    
    for num in nums:
        while theNum != num:
            missing_nums.append(theNum)
            theNum += digit
        theNum += digit

    return missing_nums


print(increment([2, 4, 6, 10, 12, 16, 18, 20, 26], 2))