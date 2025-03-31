"""Given an integer k and array arr. Your task is to return the position of the first occurrence of k in the given array and if element k is not present in the array then return -1.

Note: 1-based indexing is followed here.

Examples:

Input: k = 16 , arr = [9, 7, 16, 16, 4]
Output: 3
Explanation: The value 16 is found in the given array at positions 3 and 4, with position 3 being the first occurrence.

Input: k=98 , arr = [1, 22, 57, 47, 34, 18, 66]
Output: -1
Explanation: k = 98 isn't found in the given array.
"""


class Solution:
    def firstOccurrence(self, k, arr):
        for i in range(len(arr)):
            if arr[i] == k:
                return i + 1  # Convert to 1-based index
        return -1  # If k is not found

# Example usage
sol = Solution()

arr1 = [9, 7, 16, 16, 4]
print(sol.firstOccurrence(16, arr1))  # Output: 3

arr2 = [1, 22, 57, 47, 34, 18, 66]
print(sol.firstOccurrence(98, arr2))  # Output: -1
