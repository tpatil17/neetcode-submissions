# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        result = self.max_sum(root)
        return result[3]

    def max_sum(self, root):

        if not root:
            return [float('-inf'),float('-inf'),float('-inf'),float('-inf')] #l,r,cur, max
        else:
            left_tree = self.max_sum(root.left)

            left_r = left_tree[1]
            left_l = left_tree[0]

            cur = root.val

            right_tree = self.max_sum(root.right)
            
            right_r = right_tree[1]
            right_l = right_tree[0]
            
            left_lvl_max = max(left_l, left_r)
            right_lvl_max = max(right_l, right_r)

            left_only = left_tree[2] # whole tree
            right_only = right_tree[2] #whole tree

            rt_max = right_tree[3]
            lt_max = left_tree[3]

      
        
            level_max = max(cur,rt_max, lt_max, left_lvl_max + cur, right_lvl_max + cur, cur + left_lvl_max + right_lvl_max )

            right_lvl_max = 0 if right_lvl_max == float('-inf') else right_lvl_max
            left_lvl_max = 0 if left_lvl_max == float('-inf') else left_lvl_max

            return [max(cur,cur+left_lvl_max),max(cur, cur+right_lvl_max),max(cur ,cur+left_lvl_max+right_lvl_max), level_max]



