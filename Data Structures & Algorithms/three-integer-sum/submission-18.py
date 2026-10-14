class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:



        nums = sorted(nums)

        def bs(left, right, target, arr):

            ind = (left+right)//2
           
            if left > right:
                return False

            if arr[ind] == target:
                return True
            else:
                if arr[ind] > target:
                    right = ind-1
                else:
                    left = ind+1
                return bs(left, right, target, arr)

        l = 0
        r = len(nums)-1
        ans = {}
        result = []
        while l < r:

            if nums[l] > 0:
                # no negative value in range [l, r]
                break
            else:
                # for ever l, find the combination
                while r > l:

                    trg = -(nums[l] + nums[r])

                    if (nums[l], nums[r]) in ans:
                        r-=1
                        continue # no duplicates
                    else:
                        # new combination
                        if bs(l+1, r-1, trg, nums):
                            ans[(nums[l], nums[r])] = 0
                            result.append([nums[l], trg, nums[r]])
                        else:
                            if trg > nums[r-1]:
                                break

                    r-=1
                l+=1
                r = len(nums)-1
        

        return result



                


