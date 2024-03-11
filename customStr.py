def customSortString(order, s ):
    newStr = ''

    for char in order:
        if char in s:
            newStr += char
    lengthOfS = len(s)
    lengthOfOrder = len(newStr)
    newStr += s[lengthOfOrder:lengthOfS]

    return newStr

print(customSortString('kpeq', 'pekeq'))