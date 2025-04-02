'''Given an array arr of distinct integers. Rearrange the array in such a way that the first element is the largest and the second element is the smallest, the third element is the second largest and the fourth element is the second smallest, and so on.

Examples:

Input: arr[] = [7, 1, 2, 3, 4, 5, 6]
Output: [7, 1, 6, 2, 5, 3, 4]
Explanation: The first element is first maximum and second element is first minimum and so on.

Input: arr[] = [1, 6, 9, 4, 3, 7, 8, 2]
Output: [9, 1, 8, 2, 7, 3, 6, 4]
Explanation: The first element is first maximum and second element is first minimum and so on.'''


class Solution:
    def rearrangeArray(self, arr):
        arr.sort()  # Sort the array first
        n = len(arr)
        result = []
        
        # Use two pointers: one for max elements (from end), one for min elements (from start)
        left, right = 0, n - 1
        while left <= right:
            if right >= left:
                result.append(arr[right])  # Add largest element
                right -= 1
            if left <= right:
                result.append(arr[left])  # Add smallest element
                left += 1
        
        return result

# Example usage:
sol = Solution()
print(sol.rearrangeArray([7, 1, 2, 3, 4, 5, 6]))  # Output: [7, 1, 6, 2, 5, 3, 4]
print(sol.rearrangeArray([1, 6, 9, 4, 3, 7, 8, 2]))  # Output: [9, 1, 8, 2, 7, 3, 6, 4]
print(sol.rearrangeArray([10, 20, 30, 40, 50]))  # Output: [50, 10, 40, 20, 30]
print(sol.rearrangeArray([5, 3, 8, 1, 4]))  # Output: [8, 1, 5, 3, 4]
