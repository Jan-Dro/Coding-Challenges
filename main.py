def trap(height):
    currentTrap = 0
    first = 0
    second = 1
    max_height = max(height)

    while second < len(height):
            if height[first] == 0:
                first += 1
                second += 1
            elif height[first] > 0:
                if height[first] <= height[second] or height[first] == max_height:
                    for i in range(first +1, second):
                        currentTrap += height[first] - height[i]
                    first = second
                second += 1
    return currentTrap


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))