class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtrack(idx, cur):

            
            if idx == len(cur):
                result.append(cur.copy())
                return
            else:
                for i in range(idx, len(cur)):

                    cur[idx], cur[i] = cur[i], cur[idx] #swap
                    backtrack(idx+1, cur)
                    cur[idx], cur[i] = cur[i], cur[idx] # back track to original
        
        backtrack(0, nums)

        return result



        