class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        i = 0 # start index
        store = {}

        def dfs(res, i):
            
            if i == len(nums):
                # max depth reached
                if res == target:
                
                    return 1
                else:
                    return 0
            if (res, i) in store:
                return store[(res, i)]
            else:
                store[(res, i)]= (dfs(res-nums[i], i+1)+dfs(res+nums[i], i+1))

                return store[(res,i )]


        ans  =dfs(0, i)

        return ans