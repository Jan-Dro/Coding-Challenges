
def threeSum(nums):
    nums.sort()
    answer = []

    for i, num in enumerate(nums):
        if num > 0:
            break
        if i > 0 and num == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            threeSums = num + nums[left] + nums[right]

            if threeSums < 0:
                left += 1
            elif threeSums > 0:
                right -= 1
            else:
                answer.append([num, nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return answer

print(threeSum([-1,0,1,2,-1,-4]))