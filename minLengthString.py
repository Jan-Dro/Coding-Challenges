def minimumLength(s):
    start = 0
    end = len(s) - 1
    s = list(s)
    count = 0

    while start < end:
        while start < end and s[start] == s[end]:
            start += 1
            end -= 1
        else:
            break

    remaining_length = end - start + 1  

    return remaining_length
print(minimumLength("aabccabba"))
        