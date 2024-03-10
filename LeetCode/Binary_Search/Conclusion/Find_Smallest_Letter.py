class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if letters[-1] < target:
            return letters[0]

        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left % len(letters)]

letters = ["c","f","j"]
target = "g"
sol = Solution()
res = sol.nextGreatestLetter(letters, target)
print(res)