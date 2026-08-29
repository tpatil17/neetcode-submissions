from collections import deque

class Node:
    def __init__(self, value):
        self.val = value
        
class Graph:

    def __init__(self, grid):
        self.graph = self.buildGraph(grid)

    
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
        rows = len(self.graph)
        cols = len(self.graph[0])
        q = deque()

       
        for i in range(rows):
            for j in range(cols):
                if self.graph[i][j].val == 0:
                    q.append((i, j))


        while q:
            r, c = q.popleft()
            dist = self.graph[r][c].val
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    node = self.graph[nr][nc]
                    if node.val == 2147483647:  
                        node.val = dist + 1
                        q.append((nr, nc)) 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        graph = Graph(grid)

        graph.buildPath()


        for i in range(len(graph.graph)):
            for j in range(len(graph.graph[i])):
                grid[i][j] = graph.graph[i][j].val

        
        return


        