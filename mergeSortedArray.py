def merge(nums1, m, nums2, n):
    finalArray = sorted(nums1[:m] + nums2[:n])
    nums1[:] = finalArray
    
    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))