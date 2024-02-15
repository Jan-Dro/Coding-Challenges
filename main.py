def largestPerimeter(nums):
    nums.sort(reverse=True)  # Sort in descending order
    for i in range(len(nums) - 2):
        if nums[i + 2] < nums[i] + nums[i + 1]:
            return nums[i] + nums[i + 1] + nums[i + 2]
    return 0  


test_case = [1, 12, 1, 2, 5, 50, 3]
print("Largest Perimeter:", largestPerimeter(test_case))


# output 12
