class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in s:

            if i == "{" or i == "[" or i == "(":
                stack.append(i)
            else:
                if len(stack) > 0:
                    if i == "}" and stack[-1] == "{":
                        stack.pop(-1)
                    elif i == "]" and stack[-1] == "[":
                        stack.pop(-1)
                    elif i == ")"and stack[-1] == "(":
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
        print(stack)
        
        if len(stack) > 0:
            return False
        else:
            return True

        