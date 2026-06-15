# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        cur = head
        ln = 0

        while cur != None:
            cur = cur.next
            ln+=1

        trg_ind = ln - n
        ind = 0

        cur = head

        if trg_ind == ind:
            cur = cur.next
            head.next = None
            head = cur
            return head

        # n > 0



        while cur != None:

            if ind+1 == trg_ind:
                #item ahead is the target
                buf = cur.next
                if buf != None:
                    cur.next = buf.next

                    buf.next = None
                    return head
                else:
                    return head
            else:
                cur = cur.next
                ind+=1
        
        return head
                