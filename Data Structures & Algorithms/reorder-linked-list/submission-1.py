# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:





        if not head or not head.next:
            return

        # ── Step 1: Find the middle ──────────────────────────────────────────
        # slow ends up at the LAST node of the first half
        # e.g. [0,1,2,3,4,5,6] → slow = node(3), fast = node(6)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # ── Step 2: Reverse the second half ─────────────────────────────────
        # Split into two independent lists first
        second = slow.next
        slow.next = None        # terminate first half

        prev = None
        while second:
            nxt      = second.next
            second.next = prev
            prev     = second
            second   = nxt
        second = prev           # head of reversed second half

        # ── Step 3: Interleave ──────────────────────────────────────────────
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next  = second
            second.next = tmp1

            first  = tmp1
            second = tmp2
            