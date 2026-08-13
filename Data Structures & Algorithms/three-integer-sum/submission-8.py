class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        result = []

        for i in range(len(nums)):

            if nums[i] > 0:
                break
            else:

                if i > 0:
                    if nums[i] == nums[i-1]:
                        continue
                
                # nums[i] is not seen before

                l = i+1
                r = len(nums)-1

                while l < r:

                    if nums[l]+ nums[r]+nums[i] == 0:
                        result.append([nums[l], nums[r], nums[i]])
                    
                        while l < r and nums[l] == nums[l+1]:
                            l+=1
                        while l < r and nums[r] == nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif nums[l]+ nums[r] +nums[i] < 0:
                        l+=1
                    else:
                        r-=1
                    #unique l and r values
        return result

        
       

                


        