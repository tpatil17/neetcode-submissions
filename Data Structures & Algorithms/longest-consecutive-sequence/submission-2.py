class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash_set = set(nums)


        ans = 0

        for num in hash_set:

            streak = 1

            if num-1 not in hash_set:

                # the start of a chain
                while num+streak in hash_set:
                    streak+=1
            ans = max(ans, streak)
        
        return ans
            

        