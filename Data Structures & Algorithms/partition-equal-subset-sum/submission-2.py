class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total//2

        dp = set()
        dp.add(0)

        ctr = len(nums)-1

        while ctr >= 0:
            new = set()
            for t in dp:
                new.add(t+nums[ctr])
                new.add(t)
            dp = new
            ctr-=1
        
        return True if target in dp else False

        
        





        