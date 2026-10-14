class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights)-1
        area = 0
    
        while l < r:

            
            max_h = min(heights[l], heights[r])
            area = max(area, max_h*(r-l))

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return area

