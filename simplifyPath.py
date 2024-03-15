def simplify(path):
    stack = []
    component =path.split('/')
    
    for char in component:
        if char == '.':
            continue
        elif char == '..':
            if stack:
                stack.pop()
        elif char:
            stack.append(char)

    newPath = '/' + '/'.join(stack)
    return newPath

print(simplify('/home//foo/'))