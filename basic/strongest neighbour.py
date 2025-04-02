'''class Solution:
    def maximumAdjacent(self, n, arr):
        # Iterate through adjacent pairs and print the maximum of each pair
        result = [max(arr[i], arr[i+1]) for i in range(n-1)]
        print(*result)  # Print the output as space-separated values

# Example usage:
sol = Solution()
sol.maximumAdjacent(6, [1, 2, 2, 3, 4, 5])  # Output: 2 2 3 4 5
sol.maximumAdjacent(2, [5, 5])  # Output: 5
sol.maximumAdjacent(5, [10, 20, 30, 40, 50])  # Output: 20 30 40 50
'''

class Solution:
    def maximumAdjacent(self, n, arr):
        # Iterate through adjacent pairs and print the maximum of each pair
        result = [max(arr[i], arr[i+1]) for i in range(n-1)]
        print(*result)  # Print the output as space-separated values

# Example usage:
sol = Solution()
sol.maximumAdjacent(6, [1, 2, 2, 3, 4, 5])  # Output: 2 2 3 4 5
sol.maximumAdjacent(2, [5, 5])  # Output: 5
sol.maximumAdjacent(5, [10, 20, 30, 40, 50])  # Output: 20 30 40 50
