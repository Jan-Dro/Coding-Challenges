def findDuplicate(nums):
    hash = {}

    for num in nums:
        if num in hash:
            return num
        else:
            hash[num] = num
    return -1


print(findDuplicate([3,3,3,3,3]))