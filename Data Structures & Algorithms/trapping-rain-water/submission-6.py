class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height)-1

        max_l = height[l]
        max_r = height[r]
        water = 0
        while l <= r:
           
            if max_l < max_r:

                if height[l] <= max_l:
                    water+= max_l - height[l]
                else:
                    max_l = height[l]
                l+=1
            else:
                if height[r] <= max_r:
                    water+= max_r - height[r]
                else:
                    max_r = height[r]
                r-=1
        
        return water