"""Given an array arr of integers and an index key(0-based index). Your task is to return the element present at the index key in the array.

Examples:

Input: key = 2 , arr = [10, 20, 30, 40, 50]
Output: 30
Explanation: The value of arr[2] is 30 .

Input: key = 4 , arr = [10, 20, 30, 40, 50, 60, 70]
Output: 50
Explanation: The value of the arr[4] is 50 .

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)"""

class Solution:
    def getElementAtIndex(self, arr: list, key: int) -> int:
        return arr[key]  # Directly access the element at index `key`

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.getElementAtIndex([10, 20, 30, 40, 50], 2))  # Output: 30
    print(solution.getElementAtIndex([10, 20, 30, 40, 50, 60, 70], 4))  # Output: 50
