class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        total = sum(nums)

        nums = set(nums)

        new_total = sum(nums)*2

        return new_total-total




        