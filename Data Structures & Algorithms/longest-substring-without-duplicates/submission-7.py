class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l = 0
        r = l+1

        if len(s)==0:
            return 0

        if len(s) == 1:
            return 1
        
        charSet.add(s[l])
        ans = 1

        while r < len(s):

            if s[r] not in charSet:
                charSet.add(s[r])
                r+=1

            elif s[r] in charSet:
                charSet.discard(s[l])
                l+=1
            
            ans = max(ans, len(charSet))
        
        return ans



            

