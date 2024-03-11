def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)

    sameNums = nums1.intersection(nums2)
    return list(sameNums)


print(intersection([1,2,2,1], [2,2,]))
    