class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
                i += 2
            else:
                i += 1



arr = [1,2,3]
arr1 = Solution()
arr1.duplicateZeros(arr)
print(arr)




# print(arr)


