"""Find the first occurrence of the string pat in the string txt. The function returns an integer denoting the first occurrence of the string pat in txt (0-based indexing).

Note: You are not allowed to use the inbuilt function. If there is no occurrence then return -1.

Examples :

Input: txt = "GeeksForGeeks", pat = "Fr"
Output: -1
Explanation: Fr is not present in the string GeeksForGeeks as substring.

Input: txt = "GeeksForGeeks", pat = "For"
Output: 5
Explanation: For is present as substring in GeeksForGeeks from index 5 (0 based indexing).

Input: txt = "GeeksForGeeks", pat = "gr"
Output: -1
Explanation: gr is not present in the string GeeksForGeeks as substring."""


class Solution:
    def firstOccurrence(self, txt, pat):
        n, m = len(txt), len(pat)
        
        for i in range(n - m + 1):  # Iterate over possible starting positions
            if txt[i:i+m] == pat:  # Check if substring matches
                return i
        return -1  # Pattern not found

# Example usage
sol = Solution()
print(sol.firstOccurrence("GeeksForGeeks", "Fr"))  # Output: -1
print(sol.firstOccurrence("GeeksForGeeks", "For"))  # Output: 5
print(sol.firstOccurrence("GeeksForGeeks", "gr"))  # Output: -1
