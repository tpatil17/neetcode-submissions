class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        adj = {} # represent the graph

        for node in range(1, n+1):
            adj[node] = []

        for src, trg, time in times:
            adj[src].append((time, trg))
        
        queue = []

        distance = {}

        visited = [False for _ in range(n)]

         # start with the source
        heapq.heapify(queue)
        
        for cpl in adj[k]:
            heapq.heappush(queue, cpl)
        
        visited[k-1] = True

        while queue:
            
            val = heapq.heappop(queue)
     
            time, node = val
            if not visited[node-1]:
                visited[node-1] = True
                distance[node] = time
           
                for tm, nxt in adj[node]:

                    heapq.heappush(queue, (tm+time, nxt))
                  
        

        
        if not all(visited):
            return -1
        else:
            return max(distance.values())








        