# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def diameterOfBinaryTree(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxDiamter = [0]

        def depth(node):
            if not node:
                    return 0
                
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            maxDiamter[0] = max(maxDiamter[0], left_depth, right_depth)
            return 1 + max(left_depth, right_depth)
        depth(root)
        return maxDiamter[0]

        