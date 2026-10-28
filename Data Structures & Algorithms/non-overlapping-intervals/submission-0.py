class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        
        ctr = 0 # the number of intervals to pop
        
        intervals = sorted(intervals) # sorted by the start times

        if len(intervals) <= 1:
            return 0

        prevEnd = intervals[0][1]

        for s, e in intervals[1:]:
            if s >= prevEnd:
                prevEnd = e # update the end to be with current
            else:
                # conflict 
                prevEnd = min(e, prevEnd)
                ctr+=1
        
        return ctr

     