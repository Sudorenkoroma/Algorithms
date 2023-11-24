class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        if not arr:
            return arr

        max_num = arr[len(arr) - 1]
        # loop in reverse
        for i in range(len(arr) - 1, -1, -1):
            # print('i-->',i)
            if arr[i] > max_num:
                (arr[i], max_num) = (max_num, arr[i])
            else:
                arr[i] = max_num
        arr[len(arr) - 1] = -1
        return arr


original_array = [17,18,5,4,6,-2]
result_array = Solution()
original_array = result_array.replaceElements(original_array)
print(original_array)
