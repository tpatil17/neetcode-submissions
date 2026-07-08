class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        hash_set = set(nums)

        longest = 0

        for i in hash_set:
            # loop until i has no predecessor in hash set

            if i-1 not in hash_set:
                cursor = i
                streak = 1

                #set the smallest number as cursor

                while cursor +1 in hash_set:
                    cursor+=1
                    streak+=1
                
                longest = max(longest, streak)
        
        return longest

        

