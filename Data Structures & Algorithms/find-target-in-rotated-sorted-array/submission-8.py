class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        if l == r:
            if target == nums[l]:
                return l
            else:
                return -1

        while l < r:

            mid = l+ (r-l)//2

            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r= mid
        
        print(nums[l])

        if nums[l] <= target <= nums[len(nums)-1]:
            nl = l
            nr = len(nums)-1
        else:
            nl = 0
            nr = l
        
        print(nl)
        print(nr)
        
        while nl < nr:
            mid = nl+ (nr-nl)//2

            if target == nums[mid]:
                return mid
            else:
                if target > nums[mid]:
                    nl = mid+1
                else:
                    nr = mid

        if target == nums[nl]:
            return nl
        
        if target == nums[nr]:
            return nr

        return -1


