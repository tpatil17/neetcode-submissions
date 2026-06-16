"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_adr = {}
        new_adr = {}

        cur = head
        ind = 0
        new_head = None
        cur_2 = None

        while cur != None:

            old_adr[cur] = ind
            new = Node(cur.val) # create new node
            new_adr[ind] = new # new adr of ind
            ind+=1
            if cur == head:
                new_head = new # asign new head
                cur_2 = new
                cur = cur.next
            
            else:
                cur_2.next = new #connect to next list
                cur_2 = cur_2.next # update cursor
                cur = cur.next
        
        # two stores with indexes and their new addresses
        print("mapped addresses")

        cur = head
        cur_2 = new_head

        while cur != None:

            if cur.random != None:
                r_ind = old_adr[cur.random]
                cur_2.random = new_adr[r_ind]
            cur = cur.next
            cur_2 = cur_2.next
        
        return new_head



            
            



        