"""Given an array arr[] of positive integers. The task is to return the count of the number of odd and even elements in the array.

Note: Return two elements where the first one in the count of odd & second one is the count of even.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: 3 2
Explanation: There are 3 odd elements (1, 3, 5) and 2 even elements (2 and 4).

Input: arr[] = [1, 1]
Output: 2 0
Explanation: There are 2 odd elements (1, 1) and no even elements."""

class Solution:
    def countOddEven(self, arr):
        odd_count = sum(1 for num in arr if num % 2 != 0)
        even_count = len(arr) - odd_count
        return (odd_count, even_count)

# Example usage
sol = Solution()
print(sol.countOddEven([1, 2, 3, 4, 5]))  # Output: (3, 2)
print(sol.countOddEven([1, 1]))           # Output: (2, 0)
