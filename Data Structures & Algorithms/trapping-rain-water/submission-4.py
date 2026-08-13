class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0

        lm = height[0]
        rm = height[-1]

        if len(height) <3:
            return 0
        
        l = 0
        r = len(height)-1

        while l < r:

            if lm > rm:

                r-=1
                if height[r] < rm:
                    water+= rm-height[r]
                else:
                    rm = height[r]
            else:

                l+=1

                if height[l] < lm:
                    water+= lm-height[l]
                else:
                    lm = height[l]
        
        return water
