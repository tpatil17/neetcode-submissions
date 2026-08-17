class Solution:
    def countSubstrings(self, s: str) -> int:

        ctr= 0

        l = 0
        r =0

        ind = 0

        while ind < len(s):

            if l < 0 or r == len(s):
                ind+=1
                l = ind
                r = ind
            else:
                
                if s[l] == s[r]:
                    ctr+=1
                    l-=1
                    r+=1
                else:
                    ind+=1
                    l = ind
                    r = ind
        
        l = 0
        ind = 1
        r = 1
        while ind < len(s):

            if l < 0 or r == len(s):
                ind+=1
                l = ind-1
                r = ind
            else:

                if s[l] == s[r]:
                    ctr+=1
                    l-=1
                    r+=1
                else:
                    ind+=1
                    l = ind-1
                    r = ind
        
        return ctr
                

        