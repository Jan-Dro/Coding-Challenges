def palindromeNumber(num):
    # if num < 0:
    #     num = abs(num)
    #     reversedNum = str(num)[::-1]
    #     reversedNum = -abs(int(reversedNum))

    if num < 0:
        return False
    
    reversedNum = str(num)[::-1] 
    if num == int(reversedNum):
        return True
    return False

print(palindromeNumber(-121))