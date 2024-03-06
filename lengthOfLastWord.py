
def lengthOfLastWord(s):
    split = s.split(' ')
    listSplit = list(reversed(split))

    for word in listSplit:
        if word == '':
            continue
        else:
            return len(word)
        
print(lengthOfLastWord(' a man on a moon '))