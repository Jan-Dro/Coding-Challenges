def maximumSubArray(nums):
    max_so_far = nums[0]
    max_ending = nums[0]
    print(len(nums))
    for i in range(1, len(nums)):
        max_ending = max(nums[i], max_ending + nums[i])
        max_so_far = max(max_ending, max_so_far)
    return max_so_far


print(maximumSubArray([5,4,-1,7,8]))

#  """first nums[0]  == 5, so max so far is 5;

#  since we are starting the iteration at 1; for the len nums == 5: 
###  first iteration:
# iteration = 1, nums[i] == 4, 5 + 4 = 9 max_so_far = 9;  9 > 5
### second iteration
# iteration = 2, nums[2] == -1, -1 + 9 = 8; max_so_far = 9; 9 > 8
### third iteration
# iteration = 3, nums[3] == 7, 7 + 9 = 15; maxSoFar = 15, 15 > 9,
### fourth iteration
# itearion = 4, nums[4] == 8, 8 + 15 = 23; maxSofar = 23, 23 > 15
# returns 23
# """