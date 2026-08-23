class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        part = []
        s_l = [i for i in s]

        def dfs(i):

            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i,len(s)):
                if s_l[i:j+1][::-1] == s_l[i:j+1]:
                    #is pal
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)

        return res

        
