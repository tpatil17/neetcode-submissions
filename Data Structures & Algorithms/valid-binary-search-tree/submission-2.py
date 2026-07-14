# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        low = float('-inf')
        high = float('inf')

        ans = self.isValid(low, root, high)

        return ans
        
    def isValid(self, low, root, high):

        if not root:
            return True
        elif not (low < root.val < high):
            return False
        else:
            return self.isValid(low, root.left, root.val) \
            and self.isValid(root.val, root.right, high)


        




        