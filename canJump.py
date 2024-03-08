


def canJump(nums):
        if len(nums) == 1:
            return True

        index = 0
        for num in nums:
            if num == 0:
                continue
            if num + index == len(nums) -1:
                print(num + index)
                return True
            else:
                index += 1
        return False


print(canJump([3,2,1,0,4]))