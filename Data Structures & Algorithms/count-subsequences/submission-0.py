class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        memo = {}

        def dfs(i_s, i_t):

            if i_t == len(t):
                # string is made
                memo[(i_s, i_t)] = 1
                return 1
            else:
                if not ( 0 <= i_s < len(s)):
                    # cannot make
                    memo[(i_s, i_t)] = 0
                    return 0
                else:
                    with_char = 0
                    without = 0
                    if s[i_s] == t[i_t]:
                        # character can be selected
                        if (i_s+1, i_t+1) in memo:

                            with_char = memo[(i_s+1, i_t+1)] # fetch stored info
                        else:
                            with_char = dfs(i_s+1, i_t+1) # create new
                            memo[(i_s+1, i_t+1)] = with_char

                    if (i_s+1, i_t) in memo:

                        without = memo[(i_s+1, i_t)] # fetch stored info
                    else:
                        without = dfs(i_s+1, i_t) # create new
                        memo[(i_s+1, i_t)] = without
                    
                    return with_char + without
        
        return dfs(0,0)



        