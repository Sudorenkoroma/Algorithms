class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        final = ""
        minim = min(len(strs[0]), len(strs[-1]))
        for i in range(minim):
            if strs[0][i] == strs[-1][i]:
                final += strs[0][i]
            else:
                break
        return final


strs = ["flow","flower","flight"]
res = Solution()
sol = res.longestCommonPrefix(strs)
print(sol)