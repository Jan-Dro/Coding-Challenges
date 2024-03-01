def removeElement(nums, val):

        start = len(nums) -1

        while start >= 0:
            if nums[start] == val:
                nums.pop(start)
            start -= 1

        return len(nums)

print(removeElement([3,3], 3))




