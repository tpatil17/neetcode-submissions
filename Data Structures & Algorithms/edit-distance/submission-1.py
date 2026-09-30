class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = {}
        
        def dfs(i1, i2):

            if i1 >= len(word1) and i2 >= len(word2):
                dp[(i1, i2)] = 0
                return 0

            elif i1 >= len(word1):
                dp[(i1, i2)] = len(word2[i2:])
                return len(word2[i2:])

            elif i2 >= len(word2):
                dp[(i1, i2)] = len(word1[i1:])
                return len(word1[i1:])
            
            else:
                if word1[i1] == word2[i2]:
                    if (i1+1, i2+1) in dp:
                        return dp[(i1+1, i2+1)]
                    else:

                        return dfs(i1+1, i2+1)
                else:
                    # try all options
                    if (i1, i2+1) in dp:
                        insert = 1+ dp[(i1, i2+1)]
                    else:
                        insert = 1 + dfs(i1, i2+1)

                    if (i1+1, i2) in dp:
                        delete = 1 + dp[(i1+1, i2)]
                    else:
                        delete = 1 + dfs(i1+1, i2)

                    if (i1+1, i2+1) in dp:
                        replace = 1 + dp[(i1+1, i2+1)]
                    else:
                        replace = 1+ dfs(i1+1, i2+1)

                    dp[i1, i2] = min(insert, delete, replace)
                    return min(insert, delete, replace)

        return dfs(0, 0)