def square_even(array, length):
    # Check for edge cases.
    if array is None:
        return None

    # Create a resultant array which would hold the result.
    result = [0] * length

    # Iterate through the original array.
    for i in range(length):
        # Get the element from index i of the input array.
        element = array[i]

        # If the index is an even number, then square the element.
        if i % 2 == 0:
            element *= element

        # Write the element into the result array.
        result[i] = element

    # Return the result array.
    return result

original_array = [1, 2, 3, 4, 5]
result_array = square_even(original_array, len(original_array))
print(result_array)