# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        if inorder == []:
            return
        else:

            root = preorder.pop(0) # extartct the root

            node = TreeNode(root)

            #find lift and right sub tree
            cur = 0
            left_in = []
            right_in = []
            while cur < len(inorder):
                if inorder[cur] == root:
                    left_in = inorder[:cur]
                    right_in = inorder[cur:]
                    break
                cur+=1
            right_in.pop(0) # delete duplicate root instance
            
            left_pre = preorder[:cur+1]
            right_pre = preorder[cur:]
            

            node.left = self.buildTree(left_pre, left_in)
            node.right = self.buildTree(right_pre, right_in)

            return node

            

            
            
