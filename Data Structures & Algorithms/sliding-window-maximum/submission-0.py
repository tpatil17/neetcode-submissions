class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []

        #first pass
        l =0
        r = k
        max_nums = 0

        while r <= len(nums):

            max_nums = max(nums[l:r])
            res.append(max_nums)
            l+=1
            r+=1

        return res




            