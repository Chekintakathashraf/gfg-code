"""You are given a binary array arr[], where each element is either 0 or 1. Your task is to rearrange the array in increasing order in place (without using extra space). You do not need to return anything; simply modify the input array.

Examples:

Input: arr[] = [1, 0, 1, 1, 0]
Output: [0, 0, 1, 1, 1]
Explanation: After arranging the elements in increasing order, elements will be as 0 0 1 1 1.

Input: arr[] = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
Output: [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
Explanation: After arranging the elements in increasing order, elements will be 0 0 0 0 1 1 1 1 1 1.

Input: arr[] = [1, 1, 1, 1]
Output: [1, 1, 1, 1]
Explanation: Since the array already contains only 1s, no change is needed."""

class Solution:
    def sortBinaryArray(self, arr):
        left, right = 0, len(arr) - 1
        
        while left < right:
            if arr[left] == 1 and arr[right] == 0:
                arr[left], arr[right] = arr[right], arr[left]
            if arr[left] == 0:
                left += 1
            if arr[right] == 1:
                right -= 1

# Example usage
sol = Solution()
arr = [1, 0, 1, 1, 0]
sol.sortBinaryArray(arr)
print(arr)  # Output: [0, 0, 1, 1, 1]

arr = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
sol.sortBinaryArray(arr)
print(arr)  # Output: [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

arr = [1, 1, 1, 1]
sol.sortBinaryArray(arr)
print(arr)  # Output: [1, 1, 1, 1]
