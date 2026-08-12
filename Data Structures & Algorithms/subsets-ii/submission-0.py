class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []

        nums = sorted(nums)

        def backtrack(idx, cur):

            if idx == len(nums):
                #end
                return
            else:

                for i in range(idx, len(nums)):
                    if i > idx and nums[i] == nums[i-1]:
                        continue

                    cur.append(nums[i])
                    backtrack(i+1, cur)
                    result.append(cur.copy())
                    cur.pop()
                return
        
        backtrack(0, [])

        return result+[[]]

        