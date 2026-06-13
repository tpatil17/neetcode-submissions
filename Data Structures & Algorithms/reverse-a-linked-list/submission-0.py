# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        buffer = None
        cur = head
        prev = cur

        while cur != None:

            cur = cur.next
            prev.next = buffer
            buffer = prev
            prev = cur
        
        return buffer
        
        


        