class Node:

    def __init__(self, char):
        self.char = char
        self.left = None
        self.right = None
        

class Graph:

    def __init__(self, grid):
        self.nodes = self.buildGraph(grid)

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

        visited = [[False for _ in range(len(self.nodes[0]))] for _ in range(len(self.nodes))]

        def dfs(r, c):
            nonlocal visited

            if r-1 >= 0:
                node = self.nodes[r-1][c]
                if not visited[r-1][c]:
                    if node.char == "1":
                        visited[r-1][c] = True
                        dfs(r-1, c)

            if r+ 1 < len(self.nodes):

                node = self.nodes[r+1][c]
                if not visited[r+1][c]:
                    if node.char == "1":
                        visited[r+1][c] = True
                        dfs(r+1, c)
            if c -1 >=0:
                node = self.nodes[r][c-1]
                if not visited[r][c-1]:
                    if node.char == "1":
                        visited[r][c-1] = True
                        dfs(r, c-1)

            if c +1 < len(self.nodes[r]):
                node = self.nodes[r][c+1]
                if not visited[r][c+1]:
                    if node.char == "1":
                        visited[r][c+1] = True
                        dfs(r, c+1)

            return           


        count = 0

        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[i])):

                node = self.nodes[i][j]

                if node.char == "1":

                    if not visited[i][j]:
                        
                        count+=1
                        visited[i][j] = True
                        dfs(i, j)
                        
        return count
                
                        





class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        graph = Graph(grid)
        ans = graph.buildPath()

        return ans


        