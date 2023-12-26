class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index1 = 0
        index2 = len(numbers)-1
        res = []
        while index1 < index2:
            if target == numbers[index1] + numbers[index2]:
                res.append(index1+1)
                res.append(index2+1)
                break
            elif target < numbers[index1] + numbers[index2]:
                index2 -= 1
            else:
                index1 += 1

        return res


numbers = [3,24,50,79,88,150,345]
target = 200
res = Solution()
sol = res.twoSum(numbers, target)
print(sol)