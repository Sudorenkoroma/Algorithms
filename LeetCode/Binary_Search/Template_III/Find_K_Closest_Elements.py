from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr)<k:
            return arr
        left, right = 0, len(arr)-1
        while left < right:
            mid = (left+right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        left, right = left- 1, left

        while right - left - 1 < k:
            if left == -1:
                right += 1
            elif right == len(arr) or (x - arr[left]) <= (arr[right] - x):
                left -=1
            else:
                right +=1

        return arr[left+1:right]



# Example usage
sol = Solution()
print(sol.findClosestElements(arr=[1, 2, 3, 4, 5, 6, 7], k=5, x=4))  # Output: [1,2,3,4]
print(sol.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))  # Output: [1,2,3,4]
