"""You are given an integer array arr[]. The task is to find the sum of it.

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.

Input: arr[] = [1, 3, 3]
Output: 7
Explanation: 1 + 3 + 3 = 7.
"""


class Solution:
    def arraySum(self, arr):
        return sum(arr)

# Example usage
sol = Solution()
print(sol.arraySum([1, 2, 3, 4]))  # Output: 10
print(sol.arraySum([1, 3, 3]))     # Output: 7
