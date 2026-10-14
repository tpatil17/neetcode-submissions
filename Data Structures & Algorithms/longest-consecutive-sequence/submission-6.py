class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # rule out sort: ologn

        hash_set = set(nums) # o(1) lookupt
        ans = 0
        for i in range(len(nums)):

            #to stsart we need the smallest element
            if nums[i]-1 in hash_set:
                continue
            else:
                start = nums[i]
                count =1
                while start+1 in hash_set:
                    count+=1
                    start+=1
                ans = max(count, ans)
        
        return ans
        