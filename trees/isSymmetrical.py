class Treenode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetrical(self, root):
        def mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return (left.val == right.val) and mirror(left.left, right.right) and mirror(left.right, right.left)
        return mirror(root.left, root.right) if root else True