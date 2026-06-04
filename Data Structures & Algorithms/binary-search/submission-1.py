class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l < r:

            mid = l+(r-l)//2

            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    r= mid
                else:
                    l=mid+1
        
        if l==r and nums[l]==target:
            return l
        
        return -1
        