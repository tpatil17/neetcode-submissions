
class Node:
    def __init__(self, val):
        self.val = val
        self.edge = False

class Graph:
    def __init__(self, board):

        self.grid = self.buildGraph(board)
        self.buildPath()
    
    def buildGraph(self, board):

        res = []

        for i in range(len(board)):
            part = []
            for j in range(len(board[i])):
                node = Node(board[i][j])
                part.append(node)
            res.append(part)
        
        return res
    

    
    def onEdge(self, r, c):
        if r+ 1 >= len(self.grid):
            return True
        elif r-1 < 0:
            return True
        elif c+1 >= len(self.grid[r]):
            return True
        elif c-1 <0:
            return True
        else:
            return False 
    
    def markEdge(self, i, j):

        rows = len(self.grid)
        cols = len(self.grid[0])
    
        if self.onEdge(i, j):
            self.grid[i][j].edge = True

            return
        else:
            if i < rows-1:
                node = self.grid[i+1][j]

                if node.val == "O" and node.edge == True:
                    self.grid[i][j].edge = True

            if j < cols-1:
                node = self.grid[i][j+1]

                if node.val == "O" and node.edge == True:
                    self.grid[i][j].edge = True

            if i > 0:
                node = self.grid[i-1][j]

                if node.val == "O" and node.edge == True:
                    self.grid[i][j].edge = True  

            if j > 0:
                node = self.grid[i][j-1]

                if node.val == "O" and node.edge == True:
                    self.grid[i][j].edge = True
            return

    def buildPath(self):

        # visit from all four directions
        rows = len(self.grid)
        cols = len(self.grid[0])

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):

                if self.grid[i][j].val == "O":
                    
                    self.markEdge(i, j)
        
        for c in range(cols):
            for r in range(rows):

                if self.grid[r][c].val == "O":
                    
                    self.markEdge(r, c)      


        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):

                if self.grid[i][j].val == "O":
                    
                    self.markEdge(i, j)    
        
        for c in range(cols-1, -1, -1):
            for r in range(rows-1, -1, -1):

                if self.grid[r][c].val == "O":
                    
                    self.markEdge(r, c)

        return # self.grid contains all O's marked as edge true


                                




   


                    
class Solution:

    def solve(self, board: List[List[str]]) -> None:

        graph = Graph(board)

        for i in range(len(board)):
            for j in range(len(board[i])):

                if not graph.grid[i][j].edge and graph.grid[i][j].val == "O":
                    board[i][j] = "X"
        
        return



        
        