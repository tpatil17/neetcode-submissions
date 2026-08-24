class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []
        
        keypad = {}

        for i in range(2, 10):

            keypad[str(i)] = []

            reach = 3
            if i == 9 or i == 7:
                reach = 4
            
            
            if i != 2:
                start = start+len(keypad[str(i-1)])
            else:
                start = 97

            for char in range(start,start+reach):
                keypad[str(i)].append(chr(char))
            
            
        # keypad is equvalent of having the phone

        res = []
        part = []

        def dfs(trg):

            if trg >= len(digits):
                res.append("".join(part))
                return
            else:
                char = digits[trg]
                for c in keypad[char]:
                    
                    part.append(c)
                    dfs(trg+1)
                    part.pop()
        
        dfs(0)

        return res
