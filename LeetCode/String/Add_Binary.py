class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers
        a_int = int(a, 2)
        b_int = int(b, 2)

        # Add the integers
        sum_int = a_int + b_int

        # Convert the sum back to a binary string
        result = bin(sum_int)[2:]

        return result

a = "1111"
b = "1111"
res = Solution()
sol = res.addBinary(a, b)
print(sol)

# print(sol)