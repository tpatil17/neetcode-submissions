class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        total = sum(nums)

        ideal = 0
        
  

        for i in range(len(nums)+1):
            ideal+= i
        
        return ideal-total
        