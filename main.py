def lengthOfLastWord(s):
    split = s.split(' ')
    split = list(split)
    newList = []

    for word in split:
        if word == '':
            continue
        else:
            newList.append(word)

    return len(newList[-1])
print(lengthOfLastWord(" fly me to the moon "))