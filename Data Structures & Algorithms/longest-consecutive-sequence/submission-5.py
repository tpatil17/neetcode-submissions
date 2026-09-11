class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        count = 0 

        hash_set = set(nums)

        for num in nums:

            if num-1 in hash_set:
                continue
            
            streak = 1
            while num+streak in hash_set:
                streak+=1
            
            count = max(count, streak)
        
        return count


 

        