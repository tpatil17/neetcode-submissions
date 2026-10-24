class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)
        cur_s = intervals[0][0]
        cur_e = intervals[0][1]

        i = 0
        ans = []

        while i < len(intervals):
           
            inter = intervals[i]
            s , e = inter

            if cur_s > e:
                ans.append(inter)
            elif cur_e < s:
                ans.append([cur_s, cur_e])
                cur_s = s
                cur_e = e
            else:
                if cur_s > s:
                    cur_s = s
                if cur_e < e:
                    cur_e = e
            i+=1

        ans.append([cur_s, cur_e])

        return ans



        