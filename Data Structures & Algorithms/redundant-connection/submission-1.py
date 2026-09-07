class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adj = {}

        for node in range(1, len(edges)+1):
            adj[node] = []
        
        cycle = set()

        visit = set()

        def find(x, y, adj):
        # is it possible to reach from x to y given the adj

            if x == y: # discovered a path to y
                return True
            else:

                if adj[x] == []: # can't go deeper
                    return False
                else:
                    for new in adj[x]:
                        if new in visit:
                            continue
                        visit.add(new)
                        if find(new, y, adj):
                            return True
                    return False
        
        for n1, n2 in edges:
  
            if n1 in cycle and n2 in cycle:
                visit = set()
                if find(n1, n2, adj):
                    # secondary path exists
                    return [n1, n2]
                else:
                    # add new path
                    adj[n1].append(n2)
                    adj[n2].append(n1)
            else:
                cycle.add(n1)
                cycle.add(n2)
                adj[n1].append(n2)
                adj[n2].append(n1)

