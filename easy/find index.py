"""Given an unsorted array arr[] of integers and a key which is present in this array. You need to write a program to find the start index( index where the element is first found from left in the array ) and end index( index where the element is first found from right in the array ) return an array of length 2 with elements start index and end index.(0 based indexing is used)

If the key does not exist in the array then return -1 for both start and end index in this case.

Examples:

Input: arr[] = [1, 2, 3, 4, 5, 5] , key = 5
Output:  [4, 5]
Explanation: 5 appears first time at index 4 and appears last time at index 5(0 based indexing)

Input: arr = [6, 5, 4, 3, 1, 2] , key = 4
Output: [2, 2]
Explanation: 4 appears first time and last time at index 2.

Input: arr = [7, 8, 6] , key = 2
Output: [-1, -1]
Explanation: Since 2 does not appear in the array, we will return -1 for both the start and end indices..

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)."""


class Solution:
    def findIndices(self, arr, key):
        start, end = -1, -1  # Initialize indices
        
        for i in range(len(arr)):
            if arr[i] == key:
                if start == -1:
                    start = i  # First occurrence
                end = i  # Update last occurrence
        
        return [start, end]

# Test cases
sol = Solution()
print(sol.findIndices([1, 2, 3, 4, 5, 5], 5))  # Output: [4, 5]
print(sol.findIndices([6, 5, 4, 3, 1, 2], 4))  # Output: [2, 2]
print(sol.findIndices([7, 8, 6], 2))  # Output: [-1, -1]
