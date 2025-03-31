"""Given an unsorted array arr. Find the count of elements less than or equal to the given element x.

Examples:

Input: x = 9, arr = [10, 1, 2, 8, 4, 5] 
Output: 5
Explanation: The 5 elements are 1, 2, 8, 4 and 5.

Input: x = 2, arr = [1, 2, 2, 5, 7, 2, 9] 
Output: 4 
Explanation: The 4 elements are 1, 2, 2 and 2."""


class Solution:
    def countOfElements(self, arr, x):
        return sum(1 for num in arr if num <= x)

# Example usage
sol = Solution()
print(sol.countOfElements([10, 1, 2, 8, 4, 5], 9))  # Output: 5
print(sol.countOfElements([1, 2, 2, 5, 7, 2, 9], 2))  # Output: 4
