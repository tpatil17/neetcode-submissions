"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        new_arr = [(inter.start, inter.end) for inter in intervals]
        new_arr = sorted(new_arr) # sort by first or start time

        stack = []
        s = 0
        e = 0

        for interval in new_arr:
            if not stack:
                stack.append(interval) # add an entry
                s, e = stack[-1]
            else:

                cur_s, cur_e = interval

                if cur_s >= e:
                    # safe
                    stack.append(interval)
                    s, e = stack[-1]
                else:
                    return False
        return True
