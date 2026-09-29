class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        memo = {}
        if len(s3) < len(s1)+len(s2):
            return False # does not use all letters

        def dfs(i_trg, i_s, i_t):
            # i_s the current index of s1, i_t the current index of s2

            if i_trg == len(s3):
                # trg can be made
                return True
            else:
                
                left = False
                right = False
                if (i_s+1, i_t, i_trg+1) in memo:
                    left = memo[(i_s+1, i_t, i_trg+1)]
                else:
                    if i_s < len(s1):
                        if s1[i_s] == s3[i_trg]:
                            # use the char
                            left = dfs(i_trg+1, i_s+1, i_t)
                            memo[(i_s+1, i_t, i_trg+1)] = left

                if (i_s, i_t+1, i_trg+1) in memo:
                    right = memo[(i_s, i_t+1, i_trg+1)]
                else:
                    if i_t < len(s2):
                        if s2[i_t] == s3[i_trg]:
                            #use it
                            right = dfs(i_trg+1,i_s, i_t+1)
                            memo[(i_s, i_t+1, i_trg+1)] = right
                
                return right or left

        return dfs(0,0,0)
