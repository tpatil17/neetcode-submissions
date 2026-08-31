from collections import deque
class Node:
    def __init__(self, value):
        self.value = value

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

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        queue = deque()

        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):

                node = self.graph[i][j]

                if node.value == 2:
                    #rotten food start
                    queue.append((i,j))
               
                    while queue:
                        r,c = queue.popleft()
                        cur = self.graph[r][c]
                        time = cur.value
                    
                        for dr, dc in directions:
                            
                            if 0 <= r+dr < len(self.graph) and 0 <= c+dc < len(self.graph[r]):
                                trg = self.graph[r+dr][c+dc]

                                if trg.value != 0:

                                    if trg.value == 1:
                                        
                       
                                        trg.value = time+1
                                        queue.append((r+dr, c+dc))
                                    else:
                                
                                        if trg.value != 2:

                                            if time+1 < trg.value:
          
                                                trg.value = time+1
                                                queue.append((r+dr, c+dc))

                                            
            


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        graph = Graph(grid)

        graph.buildPath()

        maxTime = 0

        for i in range(len(graph.graph)):
      
            for j in range(len(graph.graph[i])):
                
                fruit = graph.graph[i][j]

                if fruit.value == 1:
                    return -1
                else:
                    maxTime = max(maxTime, fruit.value-2)

        

        
        return maxTime
        