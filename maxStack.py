class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, x):
        self.stack.append(x)
        if not self.maxStack or x >= self.maxStack[-1]:
            self.maxStack.append(x)

    def pop(self):
        x = self.stack.pop()
        if x == self.maxStack[-1]:
            self.maxStack.pop()
        return x

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.maxStack[-1]

    def popMax(self):
        max_elem = self.maxStack.pop()
        buffer = []
        while self.stack[-1] != max_elem:
            buffer.append(self.pop())
        self.pop()
        while buffer:
            self.push(buffer.pop()) 
        return max_elem