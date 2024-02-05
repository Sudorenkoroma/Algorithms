class Solution:
    def decodeString(self, s: str) -> str:
        curren_numb = 0
        stack = []
        last_word = ""
        for val in s:
            if val.isdigit():
                curren_numb = curren_numb * 10 + int(val)
            elif val == "[":
                stack.append(last_word)
                stack.append(curren_numb)
                last_word = ""
                curren_numb = 0
            elif val == "]":
                numb = stack.pop()
                pre_word = stack.pop()
                last_word = pre_word + numb * last_word
            else:
                last_word += val
        return last_word


s = "3[a]2[bc]"
sol = Solution()
res = sol.decodeString(s)
print(res)
