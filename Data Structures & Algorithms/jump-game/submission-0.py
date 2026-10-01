class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [False for _ in nums]

        for i in range(len(nums)-1, -1, -1):

            if i == len(nums)-1:
                dp[i] = True
            else:
                max_jump = nums[i]
                if max_jump+i >= len(nums)-1:
                    dp[i] = True
                else:
                    dp[i] = any(dp[i+1:i+max_jump+1])
        
        return dp[0]