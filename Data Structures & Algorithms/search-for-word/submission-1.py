class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        target = word[0] #the start of the word
        ans = False
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        rows = len(board)
        cols = len(board[0])


        def backtrack(count, i, j):

            if count == len(word):
                return True

            else:

                if 0 <= i < rows and 0 <= j < cols:

                    if board[i][j] == word[count]:
                        if visited[i][j] == True:
                            return False
                        
                        visited[i][j] = True
                        res = (backtrack(count+1, i-1,j) or
                        backtrack(count+1, i, j-1) or
                        backtrack(count+1, i+1, j) or
                        backtrack(count+1, i, j+1))
                        visited[i][j] = False
                        return res
                    else:
                        return False
                else:
                    return False




        for i in range(len(board)):
            for j in range(len(board[i])):
        
                if backtrack(0,i,j):
                    return True
                    
                
        
        return False



        