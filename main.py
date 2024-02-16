def canBeIncreasing(nums):
    # first = 0
    # second = 1
    # while second <= len(nums) - 1:
    #     if nums[first] < nums[second]:
    #         print(nums[first], nums[second])
    #         increasing = True
    #         first += 1
    #         second += 1
    #     else:
    #         nums.pop(first)
    #         print(nums)
    #         break

    # index = 0
    # index2 = 1
    # while index2 <= len(nums) -1:
    #     if nums[index] < nums[index2]:
    #         index += 1
    #         index2 += 1
    #     else:
    #         return False
    # return True


    def isIncreasing(after_removal):
        for i in range(1, len(after_removal)):
            if after_removal[i-1] >= after_removal[i]:
                return False
        return True

    removed = False
    i = 0
    while i < len(nums) - 1:
        if nums[i] >= nums[i + 1]:
            if removed:
                # Already removed an element before and found another non-increasing pair
                return False
            # Remove the element that disturbs the strictly increasing order the least
            if i == 0 or nums[i + 1] > nums[i - 1]:
                nums.pop(i)  # Prefer removing current element if possible
            else:
                nums.pop(i + 1)  # Remove next element otherwise
            removed = True
            # Do not increment i to compare the new pair at position i
        else:
            i += 1  # Move to the next pair if current pair is strictly increasing

    return True if removed else isIncreasing(nums) 
    
        


print(canBeIncreasing([105,924,32,968]))