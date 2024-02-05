class Solution:
    def numSquares(self, n: int) -> int:
        # Create a list to store the least number of perfect squares for each number from 1 to n
        dp = [float('inf')] * (n + 1)

        # Initialize the first element as 0, since 0 requires 0 perfect squares
        dp[0] = 0

        # Calculate the least number of perfect squares for each number from 1 to n
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]



n = 12
sol = Solution()
res = sol.numSquares(n)
print(res)