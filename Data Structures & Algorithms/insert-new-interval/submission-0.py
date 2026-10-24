class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        new_start, new_end = newInterval

        ans = []

        for inter in intervals:

            start, end = inter

            if end < new_start:
                ans.append(inter)
            elif new_end < start:
                ans.append([new_start, new_end])
                new_start = start
                new_end = end
            else:
                # increase the interval bounds by merging
                if start < new_start:
                    new_start = start
                if end > new_end:
                    new_end = end
        
        ans.append([new_start, new_end])

        return ans

        