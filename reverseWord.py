def reverseWords(s):
    newAns = []
    s = s.split(' ')
    print(s)
    for word in s:
        newAns.append(word[::-1])
        # newAns += word[::-1]


    string = ' '.join(newAns)
    return string

    


print(reverseWords('Lets take leetcode contest'))