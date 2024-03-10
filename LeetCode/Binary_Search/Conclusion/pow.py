class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 1, num
        while left <= right:
            mid = (left+right) // 2
            sqrd = mid * mid
            if sqrd == num:
                return True
            elif sqrd < num:
                left = mid + 1
            else:
                right = mid - 1

        return False


num = 14
res = Solution()
sol = res.isPerfectSquare(num)
print(sol)