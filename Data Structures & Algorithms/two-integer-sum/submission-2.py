class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_set = {}

  

        for i in range(len(nums)):

            hash_set[nums[i]] = i
        
        for j in range(len(nums)):

            n1 = nums[j]
            sub = target-n1

            if sub in hash_set:

                if hash_set[sub] != j:

                    return [j, hash_set[target-n1]]
        
