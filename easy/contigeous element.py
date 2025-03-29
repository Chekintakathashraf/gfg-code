"""Given an array arr. Determine if all the unique elements are contiguous integers.

Example:

Input: arr[] = [5, 2, 3, 6, 4, 4, 6, 6]
Output: Yes
Explanation: The elements of array form a contiguous set of integers which is [2, 3, 4, 5, 6] so the output is "Yes".

Input: arr[] = [10, 14, 10, 12, 12, 13, 15] 
Output: No
Explanation: The elements of array form a contiguous set of integers which is [10, 12, 13, 14, 15] so the output is "No".

Expected Time Complexity: O(nlog(n)).
Expected Auxiliary Space: O(n)."""

def areElementsContiguous(arr):
    unique_elements = set(arr)  # Get unique elements
    min_val, max_val = min(unique_elements), max(unique_elements)

    # Check if all numbers in range [min, max] are present
    return "Yes" if len(unique_elements) == (max_val - min_val + 1) else "No"

# Example Test Cases
print(areElementsContiguous([5, 2, 3, 6, 4, 4, 6, 6]))  # Output: "Yes"
print(areElementsContiguous([10, 14, 10, 12, 12, 13, 15]))  # Output: "No"
