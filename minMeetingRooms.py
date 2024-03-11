def minMeetingRooms(nums):
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i][0] < nums[i + 1][1]:
            print('less')
            



print(minMeetingRooms([[0,30], [5,10], [15,20]]))