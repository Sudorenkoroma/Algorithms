class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "{[(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last == "(":
                    right = ")"
                if last == "[":
                    right = "]"
                if last == "{":
                    right = "}"
                if right != i:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


s = "("
sol = Solution()
res = sol.isValid(s)
print(res)