class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        ast = []

        for i in range(len(s)):

            if s[i] == "(":
                stack.append(i)
            elif s[i] == "*":
                ast.append(i)
            else:
                if not ast and not stack:
                    return False
                else:
                    if stack:
                        stack.pop()
                    else:
                        ast.pop()
        
        while ast and stack:
            if stack.pop() > ast.pop():
                return False
        return not stack
                    



        