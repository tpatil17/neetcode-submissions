class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        result = []

        candidates = sorted(candidates)

        def dfs(i, cur, total):

            if total == target:
            
                result.append(cur.copy())

            else:

                j = i
                
                while j < len(candidates):

                    num = candidates[j]

                    if total+num > target:
                        return
                    else:

                        cur.append(num)
                        dfs(j+1, cur, total+num )

                        past  = cur.pop()

                        j+=1

                        while j < len(candidates) and candidates[j] == past:
                            
                            j+=1
                            #avoid repeated route

                return
        
        dfs(0, [], 0)

        return result

