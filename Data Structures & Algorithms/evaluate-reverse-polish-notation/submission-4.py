class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operations = ['+', '-', '*', '/']

        for i in tokens:
            print(stack)

            if i not in operations:
                stack.append(int(i))
            else:
                if i == '*':
                    n = stack.pop(-1)
                    m = stack.pop(-1)
                    ans = m*n
                    stack.append(ans)
                elif i == "/":
                    n = stack.pop(-1)
                    m = stack.pop(-1)
                    ans = m/n
                    stack.append(int(ans))
                elif i == "+":
                    n = stack.pop(-1)
                    m = stack.pop(-1)
                    ans = m+n
                    stack.append(ans)
                else:
                    n = stack.pop(-1)
                    m = stack.pop(-1)
                    ans = m-n
                    stack.append(ans)

        return stack[0]                 

        