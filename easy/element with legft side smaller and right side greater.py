"""Given an unsorted array of arr. Find the first element in an array such that all of its left elements are smaller and all right elements of its are greater than it.

Note: Return -1 if there is no such element.

Examples : 

Input: arr = [4, 2, 5, 7]
Output: 5
Explanation: Elements on left of 5 are smaller than 5 and on right of it are greater than 5.

Input: arr = [11, 9, 12]
Output: -1
Explanation: As no element here which we can say smaller in left & greater in right."""

def find_element(arr):
    n = len(arr)
    if n < 3:
        return -1  # No possible middle element in arrays of size < 3
    
    prefix_max = [0] * n
    suffix_min = [0] * n

    # Compute prefix_max[]
    prefix_max[0] = float('-inf')  # No elements on left of arr[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i - 1], arr[i - 1])

    # Compute suffix_min[]
    suffix_min[n - 1] = float('inf')  # No elements on right of arr[n-1]
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(suffix_min[i + 1], arr[i + 1])

    # Find first valid index
    for i in range(1, n - 1):
        if prefix_max[i] < arr[i] < suffix_min[i]:
            return arr[i]

    return -1  # No valid element found

# Test cases
print(find_element([4, 2, 5, 7]))     # Output: 5
print(find_element([11, 9, 12]))      # Output: -1
print(find_element([3, 4, 2, 5, 7]))  # Output: 5
print(find_element([1, 2, 3, 4, 5]))  # Output: 3 (smallest valid element)
