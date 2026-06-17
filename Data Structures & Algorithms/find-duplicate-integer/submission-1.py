class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        store = {}

        for i in nums:
            if i in store:
                return i
            else:
                store[i] = 1
        
        

        