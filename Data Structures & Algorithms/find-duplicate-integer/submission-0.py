class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        cur = 0
        
        while cur < len(nums):

            for i in range(cur+1, len(nums)):
                if nums[i] == nums[cur]:
                    return nums[i]
            cur+=1
        
        

        