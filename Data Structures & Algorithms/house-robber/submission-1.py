class Solution:
    def rob(self, nums: List[int]) -> int:

        money = []

        for i in range(len(nums)):

            if i == 0:
                money.append(nums[i])
            else:
                if i-2 < 0:
                    money.append(nums[i])
                else:
                    if i-3 < 0:
                        money.append(nums[i]+money[i-2])
                    else:

                        money.append(nums[i]+max(money[i-2], money[i-3]))
        
        return max(money)
        