def winnerOfGame(colors):
    first = 'A'
    second = 'B'
    index = 0
    index1 = 1
    index2 = 2

    # for i in range(len(colors)):
            
    if colors[index1] == first and colors[index1] == colors[index] and colors[index1] == colors[index2]:
        colors.pop(index1)

    return colors

print(winnerOfGame('AAABABA'))
