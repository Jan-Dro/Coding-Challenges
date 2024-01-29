def isValid(s):
    checker = {
        ']': '[',
        '}': '{',
        ')': '('
    }

    stack = []
    for char in s:
        if char in checker.values():
            stack.append(char)
        elif char in checker:
            if not stack or stack.pop() != checker[char]:
                return False

    return not stack



print(isValid("()[]{}"))