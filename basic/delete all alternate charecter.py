'''Given a string s as input. Delete the characters at odd indices of the string. Return the final string after deletion of characters at odd indices.

Examples :

Input: s = "Geeks"
Output: "Ges" 
Explanation: Deleted "e" at index 1 and "k" at index 3.

Input: s = "GeeksforGeeks"
Output: "GesoGes"
Explanation: Deleted e, k, f, r, e, k at index 1, 3, 5, 7, 9, 11.


Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(|s|)
'''

class Solution:
    def deleteOddIndices(self, s):
        return s[::2]  # Select characters at even indices

# Example usage:
sol = Solution()
print(sol.deleteOddIndices("Geeks"))         # Output: "Ges"
print(sol.deleteOddIndices("GeeksforGeeks")) # Output: "GesoGes"
print(sol.deleteOddIndices("abcdef"))        # Output: "ace"
