def zigzag(s, num):
    numRows = []
    for i in range(num):
        numRows.append([])

    increasing = True        
    index = 0
    for char in s:
        numRows[index].append(char)

        if increasing:
            index += 1
            if index == num -1:
                increasing = False
        else:
            index -= 1
            if index == 0:
                increasing = True
    finalString = ''.join([''.join(row) for row in numRows])
    return finalString




print(zigzag('paypalishiring', 3))