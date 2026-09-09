class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        visited = {}

        for word in wordList:
            visited[word] = False
        
        adj = {}
        adj[beginWord] = []

        # special case for start word
        def charMatch(trg, optrg):
            count = 0

            for i in range(len(trg)):
                if trg[i] != optrg[i]:
                    count+=1
            return count

        for word in wordList:

            if charMatch(beginWord, word) == 1:

                adj[beginWord].append(word)
        
        for word in wordList:
            adj[word] = []
        
        for word in wordList:

            start = word

            for trg in wordList:

                if start != trg:

                    if charMatch(start, trg) == 1:
                        adj[start].append(trg)

        # adj list representing a graph of words that are valid transformations 

        distance = {}           

        def dfs(prev, start, target):
            nonlocal visited
            if start == target:

                return 0
            else:

                if adj[start] == []:
                    # can't reach word
                    return float('inf')
                if start in distance:
                    return distance[start]
                else:
                    count = float('inf')
                    for new in adj[start]:

                        if new != prev and not visited[new]:
                            visited[new] = True
                            dist = dfs(start, new, target)
                            count = min(1 + dist, count)
                            distance[new] = dist
                            visited[new] = False

                    return count
        
        val = dfs(None , beginWord, endWord)

        if val == float('inf'):
            return 0
        else:
            return 1 + val


        