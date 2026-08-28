"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node

        new  = Node()
        new.val = node.val

        address = {}
        address[new.val] = new

        def dfs(new, node):
            if not node.neighbors:
                return
            else:
                for n in node.neighbors:

                    if n.val not in address:
                        #create node
                        newNode = Node()
                        newNode.val = n.val
                        address[n.val] = newNode
                        new.neighbors.append(newNode)
                        dfs(newNode, n)
                    else:
                        new.neighbors.append(address[n.val])
        
        dfs(new, node)



        return new
        