
def countAndSay(n):
    if n == 1:
        return '1'
    
    x = countAndSay(n -1)
    s = ''

    y = x[0]

    count = 1

    for i in range(1, len(x)):
        if x[1] == y:
            count +=1 
        else:
            s += str(count)
            s += str(y)
            y = x[i]
            count = 1
    s += str(count)
    s == str(y)
    return s

print(countAndSay(4))