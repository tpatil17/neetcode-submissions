class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return 0

        l = 0
        r = 0

        fq = {}

        max_f = 1

        fq[s[l]] = 1

        char = s[l]
        ans = 1
        while r < len(s):

            window = r-l +1

            if window-max_f <= k:

                ans = max(ans, window)

                r+=1

                if r == len(s):
                    break

                if s[r] in fq:
                    fq[s[r]] +=1
                else:
                    fq[s[r]] = 1
                
                if fq[s[r]] > max_f:
                    max_f = fq[s[r]]
                    char = s[r]
            else:

                fq[s[l]] -=1

                if char == s[l]:
                    max_f-=1
                l+=1

                for key, v in fq.items():

                    if v > max_f:
                        max_f = v
                        char = key


        
        return ans

                
