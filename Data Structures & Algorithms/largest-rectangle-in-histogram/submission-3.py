class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []

        ar = 0 # max area till now

        for i in range(len(heights)):

            if stack == []:

                stack.append((heights[i], i))
            else:
                back_ind = i

                while stack != []:

                    if stack[-1][0] > heights[i]:
                        # height cannot exceed the ith index
                        ht, ind = stack.pop(-1) # height and the position

                        buf = ht*(i-ind) 

                        back_ind = ind

                        ar = max(ar, buf)

                    elif stack[-1][0] < heights[i]:

                        stack.append((heights[i], back_ind))

                        break
                    
                    else:
                        break
                
                if stack == []:
                    stack.append((heights[i], back_ind))
                
                
            # post the while loop we have an updated stack
            # such that each height is in ascending order
        mark = len(heights)

        while stack:
            ht, ind = stack.pop(-1)
            ar = max(ar, ht*(mark-ind))

        return ar

        















        