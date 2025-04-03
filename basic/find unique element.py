'''Given an array of elements occurring in multiples of k, except one element which doesn't occur in multiple of k. Return the unique element.

Examples:

Input: k = 3, arr[] = [6, 2, 5, 2, 2, 6, 6]
Output: 5
Explanation: Every element appears 3 times except 5.

Input: k = 4, arr[] = [2, 2, 2, 10, 2]
Output: 10
Explanation: Every element appears 4 times except 10.

Expected Time Complexity: O(n* log(arr[i]))
Expected Auxiliary Space: O(log(arr[i]))'''


from collections import defaultdict

class Solution:
    def findUnique(self, arr, k):
        freq = defaultdict(int)

        # Count occurrences
        for num in arr:
            freq[num] += 1

        # Find the element that does not appear in multiples of k
        for num, count in freq.items():
            if count % k != 0:
                return num

# Example usage:
sol = Solution()
print(sol.findUnique([6, 2, 5, 2, 2, 6, 6], 3))  # Output: 5
print(sol.findUnique([2, 2, 2, 10, 2], 4))       # Output: 10
print(sol.findUnique([7, 7, 7, 7, 3], 4))        # Output: 3

class Solution:
    def findUnique(self, arr, k):
        freq = {}  # Dictionary to store occurrences

        # Count occurrences
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Find the unique element whose count is not a multiple of k
        for num in freq:
            if freq[num] % k != 0:
                return num

# Example usage:
sol = Solution()
print(sol.findUnique([6, 2, 5, 2, 2, 6, 6], 3))  # Output: 5
print(sol.findUnique([2, 2, 2, 10, 2], 4))       # Output: 10
print(sol.findUnique([7, 7, 7, 7, 3], 4))        # Output: 3
