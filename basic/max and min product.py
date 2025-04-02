'''Given two arrays of arr1 and arr2, the task is to calculate the product of the maximum element of the first array arr1, and minimum element of the second array arr2.

Examples :

Input : arr1 = [5, 7, 9, 3, 6, 2],  arr2 = [1, 2, 6, 1, 9]
Output : 9
Explanation: The max in arr1 is 9. The min element in arr2 is 1. The product is 9*1 = 9.

Input : arr1 = [0, 0, 0, 0],  arr2 = [1, 1, 2]
Output : 0

Expected Time Complexity: O(n + m).
Expected Auxiliary Space: O(1).'''


class Solution:
    def maxMinProduct(self, arr1, arr2):
        max1 = max(arr1)  # Find max in arr1 (O(n))
        min2 = min(arr2)  # Find min in arr2 (O(m))
        return max1 * min2  # Return the product

# Example usage:
sol = Solution()
print(sol.maxMinProduct([5, 7, 9, 3, 6, 2], [1, 2, 6, 1, 9]))  # Output: 9
print(sol.maxMinProduct([0, 0, 0, 0], [1, 1, 2]))  # Output: 0
print(sol.maxMinProduct([-3, -1, -7, -5], [4, 2, 6]))  # Output: -6
