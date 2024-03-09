def getCommon(nums1, nums2):
        list1 = set(nums1)
        list2 = set(nums2)

        sameNums = list1.intersection(list2)
        if sameNums:
            minNum = min(sameNums)
            return minNum
        else:
            return -1


print(getCommon([1,2,3,6],[2,3,4,5]))