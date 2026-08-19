class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        
        dp = [0]
        coins = sorted(coins)
        for trg in range(1,amount+1):

            for i in range(len(coins)):

                denom = coins[i]

                if denom > trg:

                    if i == 0:
                        dp.append(-1)
                    else:
                        break
                else:

                    if i == 0:

                        if dp[trg-denom] == -1:
                            dp.append(-1)
                        else:
                            dp.append(1 + dp[trg-denom])
                    else:
                        if dp[trg-denom] == -1:
                            continue
                        else:
                            new= dp[trg-denom]+1

                            if dp[trg] == -1:
                                dp[trg] = new
                            else:
                                dp[trg]= min(dp[trg], new)
       
       
        return dp[amount]

            

        

        

        