class Solution(object):
    def twoSum(self, nums, target):
        complementedNums = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in complementedNums:
                return [complementedNums[complement], i]
            
            complementedNums[num] = i

        return []
    
nums = [2,7,11,15]
target = 9
solution = Solution()
results = solution.twoSum(nums, target)
print(results)