class Node:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self, grid):
        self.grid = self.buildGraph(grid)
    
    def buildGraph(self, grid):
        res = []
        for i in range(len(grid)):
            part = []
            for j in range(len(grid[i])):
                new = Node(grid[i][j])
                part.append(new)
            res.append(part)
        
        return res
    
    def buildPath(self):

        visited = [[False for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]

        def dfs(r, c):

            #for any given coordinate connect all 1's
            nonlocal visited
            up = 0
            down = 0
            right = 0
            left = 0

            if r-1 >= 0:
                if not visited[r-1][c] and self.grid[r-1][c].value == 1:
                    visited[r-1][c] = True
                    up = dfs(r-1, c)

            if c-1 >= 0:
                if not visited[r][c-1] and self.grid[r][c-1].value == 1:
                    visited[r][c-1] = True
                    left = dfs(r, c-1)

            if r+1 < len(self.grid):
                if not visited[r+1][c] and self.grid[r+1][c].value == 1:
                    visited[r+1][c] = True
                    down = dfs(r+1, c)

            if c+1 < len(self.grid[r]) and self.grid[r][c+1].value == 1:
                if not visited[r][c+1]:
                    visited[r][c+1] = True
                    right  = dfs(r, c+1)
            
            return 1 + left + right + up + down
        
        ans = 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):

                if self.grid[i][j].value == 1 and not visited[i][j]:
                    
                    visited[i][j] = True
                    area = dfs(i,j)
                    ans = max(ans, area)
 
        return ans
        
            
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        graph = Graph(grid)

        maxArea = graph.buildPath()

        return maxArea
        
