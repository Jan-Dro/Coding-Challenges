def pathway(path):
    # newPath = ''
    # lastChar = ''
    # index = 0
    # for char in path:
    #     if char == '/' and lastChar == '/':
    #         index += 1
    #         continue
    #     elif char == '.':
    #         index += 1
    #         continue
    #     else:
    #         newPath += char
    #         lastChar = char
    #         index += 1
    
    # if newPath.endswith('/'):
    #     newPath = newPath[:-1]
    # return newPath

    newPath = ''
    stack = []
    components = path.split('/')

    for char in components:
        if char == '.':
            continue
        elif char == '..':
            if stack:
                stack.pop()
        elif char:
            stack.append(char)

    newPath = '/' + '/'.join(stack)
    return newPath if path  else '/'


print(pathway('/home//foo/'))