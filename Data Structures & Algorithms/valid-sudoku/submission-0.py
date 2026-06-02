class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = {}
        col = {}
        grid = {}

        #check for all the rows
        for i in range(len(board)):
            for j in range(len(board)):

                grid_no = ((i//3) , (j//3))

                if board[i][j] != ".":

                    if i in row:
                        if board[i][j] in row[i]:
                            return False
                        else:
                            row[i].append(board[i][j])
                    else:
                        row[i] = [board[i][j]]
                    
                    if j in col:
                        if board[i][j] in col[j]:
                            return False
                        else:
                            col[j].append(board[i][j])
                    else:
                        col[j] = [board[i][j]]
                    
                    if grid_no in grid:
                        if board[i][j]in grid[grid_no]:
                            return False
                        else:
                            grid[grid_no].append(board[i][j])
                    else:
                        grid[grid_no] = [board[i][j]]
                    
                    

        return True


                
