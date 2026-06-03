class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        area = 0
        heights = heights + [0]

        for i in range(len(heights)):
            
            h = heights[i]
            start = i
            if stack == []:
                stack.append((h, i))
            else:

                if h >= stack[-1][0]:
                    stack.append((h, i))
                else:
                    
                    while stack != [] and stack[-1][0] > h:

                        nh , ni= stack.pop(-1)
                        area = max(area, nh*(i-ni))
                        start = ni
                        
                    stack.append((h, start))
        
            
        return area







        