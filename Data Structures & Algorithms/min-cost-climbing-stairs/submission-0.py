class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [cost[0], cost[1]]

        if len(cost) < 3:
            
            if len(cost) == 1:
                return cost[0]
            else:
                return min(cost[0], cost[1])
        
        for i in range(2, len(cost)+1):

            if i == len(cost):
                return min(dp[i-1],dp[i-2])
            else:
                cst = cost[i]
                dp.append(cst+ min(dp[i-1],dp[i-2]))
        
        
        