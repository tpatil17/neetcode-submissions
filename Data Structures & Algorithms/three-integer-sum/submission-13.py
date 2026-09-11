class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        res = []

        for i in range(len(nums)):

            if i > 0:

                if nums[i-1] == nums[i]:
                    continue
            
            if nums[i] > 0:
                break
            
            else:

                l = i+1
                r = len(nums)-1

                while l < r:

                    total = nums[i] + nums[l] + nums[r]

                    if total == 0:

                        res.append([nums[i], nums[l], nums[r]])

                        while l < r and nums[l] == nums[l+1]:
                            l+=1
                        while l < r and nums[r] == nums[r-1]:
                            r-=1
                        
                        # move to next spot
                        l+=1
                        r-=1
                    elif total < 0:
                        l+=1
                    else:
                        r-=1
                        
        return res



        
       

                


        