

def valid(s):
    hash = {
        '}': '{',
        ')': '(',
        ']': '['
    }


    stack = []

    for char in s:
        if char in hash.values():
            stack.append(char)

        elif char in hash:
            if not stack or stack.pop() != hash[char]:
                return False
        return not stack
    

    