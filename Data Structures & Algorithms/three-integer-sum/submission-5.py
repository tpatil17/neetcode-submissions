class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        ans= []

        for i in range(len(nums)):

            #early exit as total can neve be 0
            if nums[i] > 0:
                break 

            #check for duplicate
            if i > 0 and nums[i]==nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            
            while l < r:

                total = nums[i]+nums[l] +nums[r]

                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l+1]==nums[l]:
                        l+=1
                    while l < r and nums[r-1]==nums[r]:
                        r-=1
                    r-=1
                    l+=1

                elif total < 0:
                        l+=1
                else:
                    r-=1

        
        return ans
            


                


        