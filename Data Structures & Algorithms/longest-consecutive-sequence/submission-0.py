class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        hash_set = set(nums)

        longest = 0

        for i in hash_set:

            if i-1 not in hash_set:
                # meaning no immediate predecessor
                cursor = i
                streak = 1

                while cursor+1 in hash_set:
                    cursor+=1
                    streak+=1
                
                longest = max(streak, longest)
        
        return longest

