def isBadVersion(version: int) -> bool:
    bad = 4
    if version == bad:
        return True
    if version > bad:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left<right:
            mid = (left+right)//2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return right



sol = Solution()
result = sol.firstBadVersion(5)
print(result)
