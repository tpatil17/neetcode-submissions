from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def dfs(i, j):

            if i >= len(s) and j >= len(p):
                return True
            
            elif j >= len(p):

                return False
            
            else:

                if j < len(p)-1:
                    # can exisit j+1 only if j is'nt the last element
                    if p[j+1] == '*':
                        # spl case
                        use = False
                        no_use = False
                        if i < len(s):
                            if p[j] == s[i]:
                                use = dfs(i+1, j) # stays on * for next option
                                no_use = dfs(i, j+2)
                            elif p[j] == ".":
                                use = dfs(i+1, j)
                                no_use = dfs(i, j+2)
                            else:
                                # cannot use
                                no_use = dfs(i, j+2)
                        else:
                            no_use = dfs(i, j+2) # no use to match empty

                        return no_use or use # return the base case
                    else:
                        # normal case
                        if i < len(s):
                            if p[j] == s[i]:
                                return dfs(i+1, j+1)
                            elif p[j] == ".":
                                return dfs(i+1, j+1)
                            else:
                                return False
                        else:
                            return False
                elif j == len(p)-1:
                    # j is the last index on p
                    if i < len(s):
                        if p[j] == s[i]:
                            return dfs(i+1, j+1)
                        elif p[j] == ".":
                            return dfs(i+1, j+1)
                        else:
                            return False
                    else:
                        return False
                else:
                    return False        

        return dfs(0, 0)           



