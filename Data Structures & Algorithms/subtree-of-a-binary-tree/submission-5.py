# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        if not root:
            return not subRoot

        return (self.isSameTree(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        # Both null → match
        if not s and not t:
            return True
        # One null, one not → mismatch
        if not s or not t:
            return False
        # Values must match, and both subtrees must match
        return (s.val == t.val and
                self.isSameTree(s.left, t.left) and
                self.isSameTree(s.right, t.right))   
        


