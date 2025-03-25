"""Given an array, arr[] construct a product array, res[] where each element in res[i] is the product of all elements in arr[] except arr[i]. Return this resultant array, res[].
Note: Each element is res[] lies inside the 32-bit integer range.

Examples:

Input: arr[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.

Input: arr[] = [12, 0]
Output: [0, 12]
Explanation: For i = 0, res[i] is 0.
For i = 1, res[i] is 12."""


def product_except_self(arr):
    n = len(arr)
    if n == 1:
        return [0]  # If there's only one element, no valid product array.

    # Initialize prefix and suffix product arrays
    res = [1] * n
    prefix = 1

    # Compute prefix products
    for i in range(n):
        res[i] = prefix
        prefix *= arr[i]  # Multiply prefix with the current element

    suffix = 1
    # Compute suffix products and multiply with prefix products
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= arr[i]  # Multiply suffix with the current element

    return res

# Test cases
print(product_except_self([10, 3, 5, 6, 2]))  # Output: [180, 600, 360, 300, 900]
print(product_except_self([12, 0]))           # Output: [0, 12]
print(product_except_self([1, 2, 3, 4]))      # Output: [24, 12, 8, 6]
print(product_except_self([5]))               # Output: [0] (Single element case)
