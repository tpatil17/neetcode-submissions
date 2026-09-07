class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = [False for _ in range(n)]

        adj = {}

        for node in range(n):
            adj[node] = []
        
        for n1, n2 in edges:

            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node):

            if adj[node] == []:
                return 
            else:
                for new in adj[node]:

                    if not visited[new]:
                        visited[new] = True
                        dfs(new)
                return 
        count = 0
        for start in range(n):

            if not visited[start]:
                count+=1
                dfs(start)
        
        return count
        