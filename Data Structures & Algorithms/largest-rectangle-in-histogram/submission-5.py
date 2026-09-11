class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []

        area = 0

        for i in range(len(heights)):

            ht = heights[i]
            ind = i

            if stack == []:
                stack.append((ht, ind))
            else:
                
                new = ind
                while stack:

                    if stack[-1][0] > ht:

                        nht, new = stack.pop()

                        area = max(area, nht*(ind-new))


                    else:
                        break
                
                stack.append((ht, new))
        
        print(stack)
        print(area)
        while stack:

            base = len(heights)

            ht, ind = stack.pop()

            area = max(area, ht*(base-ind))
        
        return area

