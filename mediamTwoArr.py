def findMedianSortedArray(nums1, nums2):
    list3= nums1 + nums2
    list3 = sorted(list3)
    lengthOflist = len(list3)
    median = lengthOflist // 2

    if lengthOflist % 2 == 1:
        return list3[median]
    else:
        return (list3[median - 1] + list3[median]) / 2.0



print(findMedianSortedArray([1,2], [3,4]))