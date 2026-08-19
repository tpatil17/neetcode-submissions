class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False]*(len(s)+1)
        dp[len(s)] = True

        i = len(s)-1

        while i >=0:
            for w in wordDict:
                if i+len(w) <= len(s) and w == s[i:i+len(w)]:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
            i-=1
        
        return dp[0]


        