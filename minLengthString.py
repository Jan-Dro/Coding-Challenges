def minimumLength(s):
    start = 0
    end = len(s) - 1
    s = list(s)
    count = 0

    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
            count += 2
        else:
            break

    remaining_length = len(s) - count
    remaining_string = ''.join(s[start:end+1])
    
    return remaining_length
print(minimumLength("ca"))
        