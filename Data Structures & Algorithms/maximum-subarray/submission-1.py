from functools import cache

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [i for i in nums]

        for i in range(len(nums)-1, -1, -1):

            if i == len(nums)-1:
                continue
            else:
                dp[i] = max(dp[i+1] + dp[i], dp[i])
        
        return max(dp)

        