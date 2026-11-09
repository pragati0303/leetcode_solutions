class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # If both nodes are empty
        if p is None and q is None:
            return True
        
        # If one is empty or values are different
        if p is None or q is None or p.val != q.val:
            return False
        
        # Check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)