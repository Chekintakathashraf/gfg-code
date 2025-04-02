'''Given an array arr of even size, the task is to find a minimum value that can be added to an element so that the array becomes balanced. An array is balanced if the sum of the left half of the array elements is equal to the sum of the right half.

Examples :

Input: arr = [1, 5, 3, 2]
Output: 1
Explanation: Sum of first 2 elements is 1 + 5  = 6, Sum of last 2 elements is 3 + 2  = 5, To make the array balanced you can add 1.

Input: arr = [1, 2, 1, 2, 1, 3]
Output: 2
Explanation: Sum of first 3 elements is 1 + 2 + 1 = 4, Sum of last three elements is 2 + 1 + 3 = 6, To make the array balanced you can add 2.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)'''


class Solution:
    def minValueToBalance(self, arr):
        n = len(arr)
        mid = n // 2  # Since the array is even-sized, split it into two halves
        
        left_sum = sum(arr[:mid])  # Sum of first half
        right_sum = sum(arr[mid:])  # Sum of second half
        
        return abs(left_sum - right_sum)  # Minimum value needed to balance the array

# Example usage:
sol = Solution()
print(sol.minValueToBalance([1, 5, 3, 2]))  # Output: 1
print(sol.minValueToBalance([1, 2, 1, 2, 1, 3]))  # Output: 2
print(sol.minValueToBalance([10, 20, 30, 40, 50, 60]))  # Output: 30
