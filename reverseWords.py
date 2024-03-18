def reverseWords(s):
    newStr = []
    s = s.split()
    index = len(s) - 1

    for word in s:
        newStr.append(s[index])
        index -= 1

    final = ' '.join(newStr)

    return final


print(reverseWords('string reveresed'))


    