class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
             if i.isdigit() or (i[0] == "-" and i[1:].isdigit()):
                stack.append(int(i))
             else:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    stack.append(int(b+a))
                if i == "-":
                    stack.append(int(b - a))
                if i == "*":
                    stack.append(int(b * a))
                if i == "/":
                    stack.append(int(b / a))
        return stack[0]



tokens = ["4","13","-5","/","+"]
sol = Solution()
res = sol.evalRPN(tokens)
print(res)