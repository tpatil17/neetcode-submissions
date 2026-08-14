class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))

    def rob1(self, nums: List[int]) -> int:

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