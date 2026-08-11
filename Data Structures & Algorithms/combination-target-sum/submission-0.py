class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)
        result = []

        def dfs(cur, currentList, total):

            if total == target:

                result.append(currentList.copy())
                return
            else:

                j = cur

                while j < len(nums):

                    num = nums[j]

                    if total + num > target:
                        # no use of trying other nums
                        return
                    else:

                        currentList.append(num)
                        dfs(j, currentList, total+num)
                        currentList.pop()

                        j+=1
                return
        


        dfs(0,[],0)

        return result
