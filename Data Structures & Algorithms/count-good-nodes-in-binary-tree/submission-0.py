# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        result = self.dfs(root, float('-inf'))

        return result


    def dfs(self, root, max_val):

        if not root:
            return 0
        else:
            if root.val >= max_val:
                max_val = root.val
                return 1 + self.dfs(root.left, max_val) + self.dfs(root.right, max_val)
            else:
                return self.dfs(root.left, max_val) + self.dfs(root.right, max_val)



        



        