# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        dg = 0
        def dfs(root):

            if not root:
                return [-1, 0]
            else:
                extract_left = dfs(root.left)
                extract_right = dfs(root.right)
                dg_left = extract_left[1]
                left = 1+ extract_left[0]
                dg_right = extract_right[1]
                right = 1 + extract_right[0]

                dg = max([dg_left, dg_right, left+right, left, right])
                
                return [max(left, right), dg]
        
        
        return dfs(root)[1]
        