#Binary

def countBits(n):
    res = [bin(i).count('1') for i in range(n + 1)]
    return res

print(countBits(5)) 