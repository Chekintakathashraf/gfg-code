"""Given an array arr[]. The task is to rotate the array by d elements where d ≤ arr.size.

Examples:

Input: arr[] = [-1, -2, -3, 4, 5, 6, 7], d = 2
Output: [-3, 4, 5, 6, 7, -1, -2]
Explanation: 
Rotate by 1: [-2, -3, 4, 5, 6, 7, -1]
Rotate by 2: [-3, 4, 5, 6, 7, -1, -2]

Input: arr[] = [1, 3, 4, 2], d = 3 
Output: [2, 1, 3, 4]
Explanation: After rotating the array three times, the first three elements shift one by one to the right."""

class Solution:
    def rotateArray(self, arr, d):
        n = len(arr)
        d = d % n  # Handle cases where d > n
        arr[:] = arr[d:] + arr[:d]  # Rotate using slicing

# Example usage
sol = Solution()
arr1 = [-1, -2, -3, 4, 5, 6, 7]
sol.rotateArray(arr1, 2)
print(arr1)  # Output: [-3, 4, 5, 6, 7, -1, -2]

arr2 = [1, 3, 4, 2]
sol.rotateArray(arr2, 3)
print(arr2)  # Output: [2, 1, 3, 4]
