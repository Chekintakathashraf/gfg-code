'''Given a string S. Count the characters that have ‘N’ number of occurrences. If a character appears consecutively it is counted as 1 occurrence.

Example 1:

Input:
S = "abc", N = 1
Output: 3
Explanation: 'a', 'b' and 'c' all have 
1 occurrence.

â€‹Example 2:

Input: 
S = "geeksforgeeks", N = 2
Output: 4
Explanation: 'g', 'e', 'k' and 's' have
2 occurrences.


Your Task:
You don't need to read input or print anything. Your task is to complete the function getCount() which takes the string S and an integer N as inputs and returns the count of the characters that have exactly N occurrences in the string. Note that the consecutive occurrences of a character have to be counted as 1.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).'''


class Solution:
    def getCount(self, S, N):
        count_map = {}  # Dictionary to store character occurrence count
        prev_char = None  # To track consecutive duplicates

        for char in S:
            if char != prev_char:  # Only count if it's not a consecutive duplicate
                count_map[char] = count_map.get(char, 0) + 1
            prev_char = char  # Update previous character

        # Count characters that appear exactly N times
        return sum(1 for value in count_map.values() if value == N)

# Example usage:
sol = Solution()
print(sol.getCount("abc", 1))  # Output: 3
print(sol.getCount("geeksforgeeks", 2))  # Output: 4
