class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights)-1

        area = 0

        while l < r:
            new = min(heights[l], heights[r])*(r-l)
            area = max(area, new)

            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        
        return area