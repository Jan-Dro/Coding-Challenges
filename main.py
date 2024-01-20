def maxProfit(prices):
    left = 0
    right = 1
    maxPrice = 0
    

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxPrice = max(maxPrice, profit)
        else:
            left = right
        right += 1
    return maxPrice


print(maxProfit([7,1,5,3,6,4]))
