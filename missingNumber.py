def missingNumber(nums):
    length = len(nums)

    sortedNums = sorted(nums)
    checker = 0

    while checker <= length:
        if sortedNums[checker] == checker:
            checker += 1
        else:
            return checker
    return length

print(missingNumber([9,6,4,2,3,5,7,0,1]))