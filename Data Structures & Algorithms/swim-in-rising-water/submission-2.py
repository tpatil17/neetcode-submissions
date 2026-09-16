class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        adj = {}

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                directions = [(-1,0), (0,-1), (1, 0), (0, 1)]

                for di, dj in directions:

                    if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[i]):

                        if (i, j) not in adj:
                            adj[(i, j)] = [(i+di, j+dj)]
                        else:
                            adj[(i, j)] += [(i+di, j+dj)]
        
        # adj list represents the nodes connected to each node in grid

        minHeap = []

        heapq.heapify(minHeap) # smallest travl cost from known to unknown

        visited = set() # track explored sets
        visited.add((0,0)) # start from origin

        #start with origin
        if not (0,0) in adj:
            return 0
        for nxt in adj[(0,0)]:
            heapq.heappush(minHeap, (grid[nxt[0]][nxt[1]], nxt))
        
        # minHeap stores the elevation and the coordinate

        t = grid[0][0] # start the timer
        target = (len(grid)-1, len(grid[0])-1) # we reach our goal

        while target not in visited:
            
            
            while minHeap[0][0] <= t:

                node = heapq.heappop(minHeap)

                if node[1] not in visited and node[0] <= t:
                    visited.add(node[1])
                    for item in adj[node[1]]:
                        if item not in visited:
                            heapq.heappush(minHeap, (grid[item[0]][item[1]], item))
                if not minHeap:
                    break
            
            #print(f" At time {t} visited {visited}")

            if target in visited:
                break

            if minHeap:

                t = minHeap[0][0]
        
        return t
            


            
        