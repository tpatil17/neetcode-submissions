# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False
        if head.next == None:
            return False
        if head.next.next == None:
            return False
        cur1 = head.next
        cur2 = head


        while cur1 != None:

            if cur1 == cur2:
                return True
            
            if not cur1.next:
                return False
            cur1 = cur1.next.next
            cur2= cur2.next
        
        return False
        