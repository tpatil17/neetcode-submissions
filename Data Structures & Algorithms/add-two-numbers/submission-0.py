# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur1 = l1
        cur2 = l2

        l1_ctr = 0
        l2_ctr = 0

        while cur1 != None:
            cur1 = cur1.next
            l1_ctr+=1
        
        while cur2 != None:
            cur2 = cur2.next
            l2_ctr += 1
        
        if l1_ctr >= l2_ctr:
            ans = l1
        else:
            ans = l2
        
        cur_a = ans
        cur1 = l1
        cur2 = l2

        carry = 0
        while cur1 != None and cur2 != None:

            ans_val = cur1.val + cur2.val+ carry
            num = int(ans_val%10)
            carry = int(ans_val//10)
            cur_a.val = num
            if cur_a.next == None:
                if carry != 0:
                    new = ListNode(carry)
                    cur_a.next = new
                    carry = 0
                    break

            cur_a = cur_a.next
            cur1 = cur1.next
            cur2 = cur2.next
        
        while carry != 0:

            if cur_a.next == None:
                ans_val = cur_a.val + carry
                carry = ans_val//10
                num = ans_val%10
                cur_a.val = num
                if carry == 0:
                    break

                new = ListNode(carry)
                cur_a.next = new
                carry = 0
                cur_a = cur_a.next
            else:
                ans_val = cur_a.val + carry
                carry = ans_val//10
                num = ans_val%10
                cur_a.val = num
                cur_a = cur_a.next
        
        return ans






