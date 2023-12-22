def strStr(haystack, needle):
    # Check if the needle is an empty string
    if not needle:
        return 0

    # Iterate through the haystack characters
    for i in range(len(haystack) - len(needle) + 1):
        # Check if the substring of haystack matches the needle
        if haystack[i:i + len(needle)] == needle:
            return i

    # If no match is found, return -1
    return -1

# Example usage
haystack = "butsad"
needle = "sad"
result = strStr(haystack, needle)
print(result)