class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = [[]]

        ind = 0

        while ind < len(nums):

            new = nums[ind] # new entry

            cell = []
            past = result[-1]
  

            if past != []:
                
                for i in range(len(past)):

                    cell.append(past[i]+[new])

            cell+=past
            cell.append([new])
            
     
            result.append(cell)

            ind+=1

        return result[-1]+ [[]]

                    
        
        