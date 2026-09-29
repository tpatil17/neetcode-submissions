class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]

        for i in range(len(coins)-1, -1, -1): # revrese loop over coins
       
            coin = coins[i]


            for j in range(amount+1):
                
                # at every value choose to either use or not use coin
                if j == 0:

                    dp[i][j] = 1 # you can choose empty set or no coin
                    continue
                trg = j
                if coin > trg:
                    # is it the only coin

                    if i == len(coins)-1:
                        continue
                    else:
                        # cannot use
                        dp[i][j] = dp[i+1][j] # carry on the other coin
                else:

                    if i == len(coins)-1:

                        dp[i][j] = dp[i][trg-coin]
                    else:
    
                        dp[i][j] = dp[i+1][trg] + dp[i][trg-coin]

        
        return dp[0][amount]


         

