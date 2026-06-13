# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = list1
        cur2 = list2
        ret = None
        cur3 = ret

        while cur1 != None and cur2 != None:

            if ret is None:
                if cur1.val <= cur2.val:
                    ret = cur1
                    cur1 = cur1.next
                    cur3 = ret
                    ret.next = None
                else:
                    ret = cur2
                    cur2 = cur2.next
                    cur3 = ret
                    ret.next = None
            else:
                if cur1.val <= cur2.val:
                    cur3.next = cur1
                    cur1 = cur1.next
                    cur3 = cur3.next 
                    cur3.next = None
                else:
                    cur3.next = cur2
                    cur2 = cur2.next
                    cur3 = cur3.next
                    cur3.next = None
        
        if cur1 != None:
            if ret != None:
                cur3.next = cur1
                return ret
            else:
                return cur1
        elif cur2 != None:
            if ret != None:
                cur3.next = cur2
                return ret
            else:
                return cur2
        else:
            return ret
