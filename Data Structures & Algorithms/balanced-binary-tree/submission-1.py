# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            
            if not root:
                return [0,True]
            else:
                h_l = height(root.left)
                ht_l = h_l[0]
                b_l = h_l[1]
                h_r = height(root.right)
                ht_r = h_r[0]
                b_r = h_r[1]
                if b_r == False or b_l == False:
                    
                    return [1+ max(ht_l, ht_r),False]

                elif abs(ht_l-ht_r) > 1:

                    return [1+ max(ht_l, ht_r),False]
                else:

                    return [1+ max(ht_l, ht_r),True]
        
        if not root:
            return True
        
        return height(root)[1]