import math

def numSquare(n):
    numStorage = []
    for num in range(1, n+1):
        sqrt_num = math.sqrt(num)
        if sqrt_num.is_integer():
            numStorage.append(num)


    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for num in numStorage:
            if num <= i:
                dp[i] = min(dp[i], dp[i - num] + 1)

    return dp[n]

print(numSquare(13))