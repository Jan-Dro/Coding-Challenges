# def findSubarrayWithGivenSum(arr, target):
#     window_sum, left = 0, 0
#     for right in range(len(arr)):
#         window_sum += arr[right]
#         while window_sum > target and left <= right:
#             window_sum -= arr[left]
#             left += 1
#         if window_sum == target:
#             return arr[left:right+1]
#     return []



def findSubarray(nums, k):
    count = 0
    current_sum = 0
    left = 0
        
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum * (right - left + 1) >= k and left <= right:
            current_sum -= nums[left]
            left += 1
        count += (right - left + 1)
            
    return count