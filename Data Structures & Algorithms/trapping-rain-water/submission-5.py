class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height)-1

        lm = height[l]
        rm = height[r]

        water = 0
        while l < r:

            if lm < rm:

                l += 1

                if height[l] >= lm:
                    lm = height[l]
                else:
                    water+= lm-height[l]

            else:
                r-=1
                if height[r] >= rm:
                    rm = height[r]
                else:
                    water+= rm - height[r]
        
        return water
  