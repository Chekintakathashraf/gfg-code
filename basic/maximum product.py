'''Given an array arr of non-negative integers, return the maximum product of two numbers possible.

Example:

Input: arr[] = [1, 4, 3, 6, 7, 0] 
Output: 42
Explanation: 6 and 7 have the maximum product.

Input: arr[] = [1, 100, 42, 4, 23]
Output: 4200
Explanation:  42 and 100 have the maximum product.'''


class Solution:
    def maxProduct(self, arr):
        # Sort the array and take the last two largest numbers
        arr.sort()
        return arr[-1] * arr[-2]  # Maximum product of two largest numbers

# Example usage:
sol = Solution()
print(sol.maxProduct([1, 4, 3, 6, 7, 0]))  # Output: 42 (6 * 7)
print(sol.maxProduct([1, 100, 42, 4, 23]))  # Output: 4200 (100 * 42)
print(sol.maxProduct([10, 20, 30, 40]))  # Output: 1200 (30 * 40)
print(sol.maxProduct([5, 2, 8, 9, 1]))  # Output: 72 (8 * 9)
