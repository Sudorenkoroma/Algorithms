class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # Ensure k is within the range of the array size
        if k == 0:
            return  # No rotation needed
        count = 0  # Count of elements that have been moved
        start = 0  # Start index for the current cycle
        while count < n:
            next_idx = start
            prev = nums[start]
            while True:
                next_idx = (next_idx + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                count += 1
                if start == next_idx:
                    break
            start += 1  # Move to the next cycle


# Example usage:
nums = [1,2,3,4,5,6,7,8,9]
k = 3
solution = Solution()
solution.rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]