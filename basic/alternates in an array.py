"""You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 1 3
Explanation:
Take first element: 1
Skip second element: 2
Take third element: 3
Skip fourth element: 4

Input: arr[] = [1, 2, 3, 4, 5]
Output: 1 3 5
Explanation:
Take first element: 1
Skip second element: 2
Take third element: 3
Skip fourth element: 4
Take fifth element: 5"""


class Solution:
    # Function to return elements in alternate order
    def alternateElements(self, arr):
        return arr[::2]  # Take every second element starting from index 0

# Example usage
sol = Solution()
print(sol.alternateElements([1, 2, 3, 4]))     # Output: [1, 3]
print(sol.alternateElements([1, 2, 3, 4, 5]))  # Output: [1, 3, 5]
print(sol.alternateElements([10, 20, 30, 40, 50, 60]))  # Output: [10, 30, 50]
