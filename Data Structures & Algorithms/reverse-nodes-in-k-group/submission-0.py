# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        def reverse(prev,head, tail, post):

            cur = head
            end = post
            #prev is None or the node before head
            #post is None or the node after tail
            while cur != end:

                if prev == None:
                    buffer = cur.next
                    cur.next = post
                    post = cur
                    cur = buffer
                else:
                    buffer = cur.next
                    cur.next = post
                    if buffer != end:
                        prev.next = buffer
                    post = cur
                    cur = buffer
            
            return

        len_list = 0

        cur = head

        while cur != None:
            len_list += 1
            cur = cur.next
        
        if k > len_list:
            return head
        
        ctr= 0

        cur = head
        start = head
        total_ctr = 0
        prev = None
        tail = None

        while cur != None:

            if k > (len_list - total_ctr):
                return head

            elif ctr == k-1:
                # mark as end of list to rev
                if prev == None:
                    tail = cur
                    cur = cur.next #move ahead of list
                    
                    reverse(prev, start, tail, tail.next)
                    head = tail #switch the head
                    prev = start
                    start = cur
                    
                    
                else:
                    tail = cur
                    cur = cur.next
                    reverse(prev,start, tail, tail.next )

                    prev = start
                    start = cur

                ctr+=1
                total_ctr+=ctr
                ctr = 0 # reset counter
                

            else:
                ctr+=1
                
                cur = cur.next
        
        return head




                    
        
