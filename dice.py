class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        mn = m + n
        nums1.extend(nums2)
        nums1.sort()
        nums1[:] = nums1[:mn]


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
res = Solution()
res.merge(nums1, m, nums2, n)

print(nums1)