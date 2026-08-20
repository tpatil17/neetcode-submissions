class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1]*len(nums)

        ind= len(nums)-1

        while ind >= 0:

            for j in range(ind+1,len(nums)):
                
                if nums[ind] < nums[j]:
                    dp[ind] = max(dp[ind], 1+ dp[j])
            ind-=1
        
        return max(dp)

