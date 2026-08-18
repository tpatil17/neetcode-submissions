class Solution:
    def numDecodings(self, s: str) -> int:

        dp = []

        for i in range(len(s)):

            if i == 0:
                #firs entry
                if int(s[i]) == 0:
                    return 0 # can't map a number with leading zero
                else:
                    dp.append((1,0))
            else:
                prev = int(s[i-1])
                cur = int(s[i])
                if prev != 0:
                    # check if greater
                    if prev > 2 and cur == 0:
                        return 0 # cannot be mapped
                    elif prev > 2:
                        wp, p = dp[-1]
                        new = wp+p
                        dp.append((new, 0))

                    elif prev == 2 and cur > 6:
                        wp, p = dp[-1]
                        new = wp+p
                        dp.append((new, 0))                      

                    else:
                        if cur == 0:
                            wp, p = dp[-1]
                            new = wp
                            dp.append((0, new))

                        else:
                            wp, p = dp[-1]
                            new = wp+p
                            pair = wp
                            dp.append((new, pair))

                else:
                    if cur == 0:
                        return 0 # two consecitive zeros
                    else:
                        wp, p = dp[-1]

                        new = p

                        dp.append((new, 0))
        
        return dp[-1][0]+dp[-1][1]

            