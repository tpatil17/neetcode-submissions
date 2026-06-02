class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers)-1

        while l < r:

            left = numbers[l]
            right = numbers[r]

            if left+right == target:
                return [l+1,r+1]
            else:

                if left+right >= target:
                    r-=1
                else:
                    l+=1

                    
        

            

            
                    

            
        