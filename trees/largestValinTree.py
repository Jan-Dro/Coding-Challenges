from collections import deque

class Treenode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def largestValues(self, root):
        # if not root:
        #     return []
        # largestVal = []
        # queue = deque([root])

        # while queue:
        #     size = len(queue)
        #     maxVal = float('-inf')

        #     for _ in range(size):
        #         node = queue.popleft()
        #         maxVal = max(maxVal, node.val)

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     largestVal.append(maxVal)
        result = []
        level = 1

        def find(self, level, root):
            if not root:
                return []
            if len(result) < level:
                result.append(root.val)
            else:
                result[level - 1] = max(result[level -1], root.val)
            find(result, level + 1, root.left)
            find(result, level +1, root.right)
        find(result, level, root)
        
        return result