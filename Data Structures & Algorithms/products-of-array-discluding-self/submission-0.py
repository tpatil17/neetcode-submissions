class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        left = []
        right = []
        
        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                left.append(left[i-1]*nums[i-1])
        
        j = len(nums)-1

        while j >=0:

            if j == len(nums)-1:
                right.append(1)
            else:
                right.append(right[-1]*nums[j+1])
            
            j-=1
        
        right = right[::-1]
        for i in range(len(nums)):
            output.append(left[i]*right[i])
        
        return output
