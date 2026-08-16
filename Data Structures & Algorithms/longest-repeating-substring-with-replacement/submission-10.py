class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}

        res = 0
        maxf = 0

        l =0
        r = 0

        while r < len(s):

            count[s[r]] = 1 + count.get(s[r], 0)

            maxf = max(count.values()) # max value in the dictionary

            print(maxf)

            while (r-l) - maxf > k-1: # while replacement clause is valid
                count[s[l]] -= 1
                l+=1

            res = max(res, (r-l)+1)
            r+=1
        
        return res






