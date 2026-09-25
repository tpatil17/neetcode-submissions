class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. Track ALL unique characters across all words
        adj = {c: set() for w in words for c in w}
        
        # 2. Compare adjacent words only
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # Invalid case: prefix rule (e.g., "abc" before "ab")
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break  # Only the first differing character matters
                    
        # 3. DFS Topological Sort
        visit = {} # False = visiting (in path), True = fully visited
        res = []
        
        def dfs(char):
            if char in visit:
                return visit[char]
            
            visit[char] = False
            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False
            
            visit[char] = True
            res.append(char)
            return True
        
        # Visit every node in adj to pick up unconstrained letters like 'd' and 'e'
        for char in adj:
            if not dfs(char):
                return ""
                
        return "".join(res[::-1])

                
                        

        