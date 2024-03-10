def guess(num: int) -> int:
    gess = 9
    if num == gess:
        return 0
    if num > gess:
        return -1
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (right + left) // 2
            res = guess(mid)
            if res == 0:
                return mid
            if res < 0:
                right = mid - 1
            else:
                left = mid + 1

        return -1

sol = Solution()
result = sol.guessNumber(2)
print(result)

