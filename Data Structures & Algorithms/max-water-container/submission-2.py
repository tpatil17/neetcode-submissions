class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0

        r = len(heights)-1

        area = 0

        while l < r:

            ht = min(heights[l], heights[r])

            area = max(area, ht*(r-l))

            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        
        return area

