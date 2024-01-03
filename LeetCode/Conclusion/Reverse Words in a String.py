class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words
        words = s.split()
        res = []
        for i in words:
            res.append(i[::-1])
        result = " ".join(res)

        # reversed_words = [word[::-1] for word in words]
        # print(reversed_words)
        #
        # # Join the reversed words with the original whitespace
        # result = ' '.join(reversed_words)

        return result

# Example usage:
s = "the sky is blue"
solution = Solution()
output = solution.reverseWords(s)
print(output)  # Output: "blue is sky the"