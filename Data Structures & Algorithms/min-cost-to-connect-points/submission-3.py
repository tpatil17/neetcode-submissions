class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adj = {}

        for i in range(len(points)):

            adj[i] = []
        
        for i in range(len(points)):
            for j in range(len(points)):

                if i == j:
                    continue
                else:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    adj[i].append((dist, j))

        # adj stores the cost to destination from each src

        minHeap = []

        heapq.heapify(minHeap)

        # initialize with origin

        for item in adj[0]:
            heapq.heappush(minHeap, item)

        visited = set()
        visited.add(0)
        cost = 0

        while len(visited) < len(points):
            nxt = heapq.heappop(minHeap)
            if nxt[1] in visited:
                continue 
            cost+=nxt[0]
            for item in adj[nxt[1]]:
                heapq.heappush(minHeap, item)
            visited.add(nxt[1])
        
        return cost
