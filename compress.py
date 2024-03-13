
# def compress(chars):
#     read, write = 0, 0

#     while read < len(chars):
#         char = chars[read] 
#         count = 0  

#         while read < len(chars) and chars[read] == char:
#             read += 1
#             count += 1

#         chars[write] = char
#         write += 1

#         if count > 1:
#             for digit in str(count):
#                 chars[write] = digit
#                 write += 1
#     return write



def compress(chars):
    left = 0
    right = 0

    while left < len(chars):
        char = chars[left]
        count = 0
        while left < len(chars) and char == chars[left]:
            left += 1
            count += 1
        chars[right] = char
        right += 1

        if count > 1:
            for digit in str(count):
                chars[right] = digit
                right += 1
    return right


print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
        
