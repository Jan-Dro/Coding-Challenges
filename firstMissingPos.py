def firstMissingPos(nums):
        oneIsThere = False
        if 1 in nums:
            oneIsThere = True
        else:
            return 1
        
        currentNum = 0
        nextNum = 1
        newNum = []
        for num in nums:
             if num < 0:
                  continue
             else:
                  newNum.append(num)

        newNum = sorted(newNum)

        while nextNum <= len(newNum) - 1:
            if newNum[currentNum] < 0:
                currentNum += 1
                nextNum += 1
            if newNum[currentNum] + 1 == newNum[nextNum] or newNum[currentNum] == newNum[currentNum + 1]:
                currentNum += 1
                nextNum += 1
            else:
                return  newNum[currentNum] + 1
        return newNum[len(newNum) - 1] + 1
            

    

print(firstMissingPos([-10,-3,-100,-1000,-239,1]))
print(firstMissingPos([1,2,0]))
print(firstMissingPos([3,4,-1,1]))
print(firstMissingPos([7,8,9,11,12]))
print(firstMissingPos([1,1001]))