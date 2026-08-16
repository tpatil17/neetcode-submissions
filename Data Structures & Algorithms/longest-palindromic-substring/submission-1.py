class Solution:
    def longestPalindrome(self, s: str) -> str:

        
        dp = []

        pal = s[0]

        for i in range(len(s)):

            if i == 0:
                dp.append([s[i]])
            else:
                buffer = []
                for char in dp[i-1]:
                    new = char+s[i]
                    buffer.append(char+s[i])
                    if new == new[::-1]:
                        pal = new if len(new) >= len(pal) else pal
                buffer.append(s[i])

                dp.append(buffer)
        
        return pal
