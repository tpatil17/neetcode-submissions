class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        

        dp = {}

        def dfs(balloons):

            if len(balloons) == 0:
                dp[tuple(balloons)] = 0
                return 0 # no ballons to burst

            elif len(balloons) == 1:
                # the only balloon has to pop
                val = balloons[0]
                dp[tuple(balloons)] = val
                return val 
            else:
                # choose either to burst or not
                best = 0 
                for j in range(len(balloons)):
                    
                    if  0 < j < len(balloons)-1:
                        temp = balloons[:j] + balloons[j+1:]
                    elif j == 0:
                        temp = balloons[1:]
                    elif j == len(balloons)-1:
                        temp = balloons[:j]
                    
                    # temp is a temporary array
                    lt = 1 if j == 0 else balloons[j-1]
                    rt = 1 if j == len(balloons)-1 else balloons[j+1]
                    coin = balloons[j]
                    if tuple(temp) in dp:
                        val = rt*coin*lt + dp[tuple(temp)]
                    else:
                        val = rt*coin*lt + dfs(temp)
                    best = max(best, val)

                dp[tuple(balloons)] = best
                return best
        
        return dfs(nums)
