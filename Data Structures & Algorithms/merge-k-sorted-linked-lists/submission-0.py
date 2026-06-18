# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        store = {}

        # go through all the nodes and store them in hash map

        for main_cur in lists:
            cur = main_cur

            while cur != None:
                if cur.val in store:
                    buf = cur.next
                    cur.next = store[cur.val][0] #point at head
                    store[cur.val][0] = cur #update new head
                    cur = buf #continue to next
 
                else:
                    store[cur.val] = [cur, cur] #[head, tail]
                    buf = cur.next
                    cur.next = None
                    cur = buf
                    #continue
        
        #store contains all nodes with appropriate values as keys
        ans = None
        tail = None
        for key in sorted(store.keys()):

            if ans == None:
                #point to head
                ans = store[key][0]
                tail = store[key][1]
            else:
                tail.next = store[key][0] #point to next element chains head
                tail = store[key][1]
        
        return ans








        