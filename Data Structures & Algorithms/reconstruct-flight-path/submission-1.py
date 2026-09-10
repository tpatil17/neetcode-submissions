class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = {}

        for src, dst in tickets:
            
            if src not in adj:
                adj[src] = [dst]
            else:
                adj[src].append(dst)
                adj[src] = sorted(adj[src], reverse= True)
                # reverse pop!
        result = []

      

        def dfs(src):
            if src not in adj:
                result.append(src)
                return

            while adj[src]:

                nxt = adj[src].pop() # lxico last

                dfs(nxt)
            
            result.append(src)
            return
        
        dfs("JFK")

        return result[::-1]
                

 
        
     