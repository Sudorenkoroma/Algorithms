class ArraySearch:
    @staticmethod
    def linear_search(array, element):
        # Check for edge cases
        if array is None or len(array) == 0:
            return False

        # Check each element starting from the first one
        for i in range(len(array)):
            # We found the element at index i, so return True.
            if array[i] == element:
                return True

        # We didn't find the element in the array.
        return False


array = [0, 1, 4, 30, 31]
element = 50
result = ArraySearch()
res = result.linear_search(array, element)

print(res)
