def firstPalindromicSeq(words):

    currentStr = ''

    for word in words:
        currentStr = word[::-1]

        if word == currentStr:
            return word
    return ''
        
print(firstPalindromicSeq(["notapalindrome","racecar"]))