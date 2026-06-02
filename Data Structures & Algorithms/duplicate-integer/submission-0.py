class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        store = []

        for i in nums:
            if i not in store:
                store.append(i)
            else:
                return True
        
        return False

        