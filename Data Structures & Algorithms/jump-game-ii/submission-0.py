class Solution:
    def jump(self, nums: List[int]) -> int:

        dp = [0 for _ in nums]

        for i in range(len(nums)-1, -1, -1):

            if i == len(nums)-1:
                dp[i] = 0
            else:
                if nums[i] == 0:
                    dp[i] = float("inf")
                else:
                    dp[i] = 1 + min(dp[i+1:i + nums[i]+1])
        return dp[0]