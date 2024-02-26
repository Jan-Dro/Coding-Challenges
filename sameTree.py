def isSameTree(self, p, q):
    if not p and not q:
        return True
    
    if not p or not q or p.val != q.val:
        return False
    

    left_side = self.isSameTree(p.left, q.left)
    right_side = self.isSameTree(p.right, q.right)

    return left_side and right_side


