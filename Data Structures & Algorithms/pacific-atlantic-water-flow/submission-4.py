
class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        def dfs(r, c, visited, prev_height):
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or visited[r][c]
                    or heights[r][c] < prev_height):   # reverse flow: must be >= to step in
                return
            visited[r][c] = True
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])                  # top border -> Pacific
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])   # bottom border -> Atlantic
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])                  # left border -> Pacific
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])   # right border -> Atlantic

        return [[r, c] for r in range(rows) for c in range(cols)
                if pacific[r][c] and atlantic[r][c]]