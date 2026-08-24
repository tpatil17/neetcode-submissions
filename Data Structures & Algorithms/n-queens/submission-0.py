class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        queens = [] #pair of (r, c) marking occupied positions
        res = []

        def dfs(row):
         
            if row >= n:
                res.append(queens.copy())
                return
            else:
                if not queens:
                    for j in range(n):
                        queens.append((row, j))
                        dfs(row+1)
                        queens.pop()
                else:

                    j = 0
                    valid = True
                    while j < n:

                        for r, c in queens:

                            dif = row - r

                            if (r, j-dif) == (r, c) or (r, j+dif) == (r, c) or j == c:
                                valid = False
                                break
                        
                        if valid:
                            queens.append((row, j))
                            dfs(row+1)
                            queens.pop()
                        else:
                            valid = True
                        

                        j+=1
    
   
        
        dfs(0)

        template = []

        for bid in range(len(res)):
            board = res[bid]
            temp = []
            for i, j in board:
                row = "."*j+"Q"+"."*(n-(j+1))
                temp.append(row)
                
            template.append(temp)




        return template






        
            

                
