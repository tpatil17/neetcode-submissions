# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        path_to_p = []

        cur = root

        while cur.val != p.val:
       
            path_to_p.append(cur)
           
            if p.val < cur.val:
                cur = cur.left
                
            else:
                cur = cur.right
            
        
        path_to_p.append(cur)

        # path to q
        path_to_q = []

        cur = root
        while cur.val != q.val:
            path_to_q.append(cur)
        

            if q.val < cur.val:
                cur = cur.left
                
            else:
                cur = cur.right
        
        path_to_q.append(cur)

        ind = 0

        while path_to_q[ind] == path_to_p[ind]:
            ind+=1

            if ind >= len(path_to_q):
                return path_to_q[ind-1]
            elif ind >= len(path_to_p):
                return path_to_p[ind-1]
        
        return path_to_p[ind-1]
        

        
        
