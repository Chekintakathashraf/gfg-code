'''Given a sorted array arr consisting of 0s and 1s. The task is to find the index (0-based indexing) of the first 1 in the given array.

NOTE: If one is not present then, return -1.

Examples :

Input : arr[] = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
Output : 6
Explanation: The index of first 1 in the array is 6.

Input : arr[] = [0, 0, 0, 0]
Output : -1
Explanation: 1's are not present in the array.

Expected Time Complexity: O(log (n))
Expected Auxiliary Space: O(1)'''


class Solution:
    def firstIndex(self, arr):
        left, right = 0, len(arr) - 1
        first_one_index = -1  # Default to -1 if 1 is not found
        
        while left <= right:
            mid = (left + right) // 2  # Find middle index
            
            if arr[mid] == 1:
                first_one_index = mid  # Update first occurrence index
                right = mid - 1  # Search in the left half for earlier occurrence
            else:
                left = mid + 1  # Move to the right half
            
        return first_one_index

# Example usage:
sol = Solution()
print(sol.firstIndex([0, 0, 0, 0, 0, 0, 1, 1, 1, 1]))  # Output: 6
print(sol.firstIndex([0, 0, 0, 0]))  # Output: -1
print(sol.firstIndex([1, 1, 1, 1]))  # Output: 0
