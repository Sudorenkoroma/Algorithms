class Solution:
    def checkIfExist(self, array: list[int]) -> bool:
        if array is None or len(array) == 0:
            return False

        num_set = set()

        for num in array:
            if num * 2 in num_set or (num / 2 in num_set):
                return True

            num_set.add(num)

        return False

arr = [-2,0,1,5,11,-19,4,6,-8]
solution = Solution()
res = solution.checkIfExist(arr)
print(res)
