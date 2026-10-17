from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        store = {}

        for word in wordDict:
            store[word] = True
        
        @cache
        def dfs(i, buf):

            if i == len(s):
                if buf in store:
                    return True
                else:
                    return False
            else:

                if buf:
                    if buf in store:
                        use_char = dfs(i+1, buf+s[i])
                        no_char = dfs(i+1, s[i])
                        return use_char or no_char

                return dfs(i+1, buf+s[i])
        
        return dfs(0, "")


        