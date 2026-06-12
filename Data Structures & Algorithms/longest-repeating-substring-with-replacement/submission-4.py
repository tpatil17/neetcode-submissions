class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {} # track the char count

        l = 0 # start

        max_fr = 0

        res = 0

        for r in range(len(s)): #r marks the end of a window

            count[s[r]] = 1+ count.get(s[r],0)

            max_fr = max(max_fr, count[s[r]])

            while (r-l+1) - max_fr > k:
                count[s[l]] -= 1
                l+=1
                    
            res= max(res, (r-l+1))
        
        return res