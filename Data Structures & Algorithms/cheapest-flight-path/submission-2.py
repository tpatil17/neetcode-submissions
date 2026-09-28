class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = {}

        for port in range(n):
            adj[port] = []
        
        for start, end, t_cost in flights:
            adj[start].append((end, t_cost))
        
        # graph connected

        memo = {} # remember explored routes

        def dfs(start, target, max_hops):

            if max_hops < 0:
                return float('inf')
            
            if (start, max_hops) in memo:
                return memo[start, max_hops]

            best = float('inf') # on every level return the best 

            for port, cost in adj[start]:
                # for each available port 
                if port == target:
                    best = min(cost, best)
                else:
                    new = cost + dfs(port, target, max_hops-1)
                    best = min(new, best)
            memo[(start, max_hops)] = best
            return best

        ans = dfs(src, dst, k)

        if ans != float('inf'):
            return ans
  
        return -1




                    
                    




