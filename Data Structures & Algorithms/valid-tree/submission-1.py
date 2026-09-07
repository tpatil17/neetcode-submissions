class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited = [False for _ in range(n)]

        adj = {}

        for node in range(n):
            adj[node] = []
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        cycle = set()

        def dfs(node, prev):

            if adj[node] == []:
                return True
            else:

                if node in cycle:
                    return False
                else:
                    cycle.add(node)
                    visited[node] = True

                    for new in adj[node]:
                        if new == prev:
                            continue
                        else:
                            if not dfs(new, node):
                                return False
                    return True
        
        if n == 0:
            return True
        if n == 1 and edges == []:
            return True
        
        val = dfs(0,None)

        if val and all(visited):
            return True
        else:
            return False
                    

