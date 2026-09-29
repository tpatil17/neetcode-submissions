class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:


        dp = {} # remember calculated paths

        def dfs(r, c):

            if not (0 <= r < len(matrix)) or not (0 <= c < len(matrix[0])):
                # the current index is out of bounds
                return 0
            else:
                # given row, col pair is valid
                cur = matrix[r][c] # the current value
                # the possible travel directions
                north = 0 
                east = 0
                south = 0
                west = 0
                if r+1 < len(matrix):
                    #can travel south
                    if matrix[r+1][c] > cur:
                        if (r+1, c) in dp:
                            south = dp[(r+1, c)]
                        else:
                            south = dfs(r+1, c)
                            dp[(r+1, c)] = south
                if r-1 >= 0:
                    # can tavel north
                    if matrix[r-1][c] > cur:
                        if (r-1, c) in dp:
                            north = dp[(r-1, c)]
                        else:
                            north = dfs(r-1, c)
                            dp[(r-1, c)] = north

                if c+1 < len(matrix[0]):
                    # can travel east
                    if matrix[r][c+1] > cur:
                        if (r, c+1) in dp:
                            east= dp[(r, c+1)]
                        else:
                            east = dfs(r, c+1)
                            dp[(r, c+1)] = east
                if c-1 >= 0:
                    # can travel west
                    if matrix[r][c-1] > cur:
                        if (r, c-1) in dp:
                            west= dp[(r, c-1)]
                        else:
                            west = dfs(r, c-1)
                            dp[(r, c-1)] = west
                
                # explore all possible directions and fetch the longes route
                best = max(north, south, east, west)
                return 1+best
        best_path = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                best_path = max(dfs(i, j), best_path)
        
        return best_path
                
        