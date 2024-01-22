#Binary

# def countBits(n):
#     res = [bin(i).count('1') for i in range(n + 1)]
#     return res

# print(countBits(5)) 



def missingNum(nums):
    nums.sort()
    
    for i, number in enumerate(nums):
        if number != i:
            return i
    return len(nums)
        

print(missingNum([0,1]))