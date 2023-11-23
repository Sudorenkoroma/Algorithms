class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)

        # Check if the array is long enough to form a mountain
        if n < 3:
            return False

        # Initialize two pointers, left and right
        left, right = 0, n - 1

        # Move the left pointer to the right until the mountain is ascending
        while left < n - 1 and arr[left] < arr[left + 1]:
            left += 1

        # Move the right pointer to the left until the mountain is descending
        while right > 0 and arr[right] < arr[right - 1]:
            right -= 1

        # Check if both pointers are not at the start or end of the array
        # and if they meet at the same index, then it's a valid mountain array
        return 0 < left == right < n - 1



array = [0, 1, 3, 4, 2, 2, 1, 4, 3, 2, 1]

result = Solution()
res = result.validMountainArray(array)

print(res)
