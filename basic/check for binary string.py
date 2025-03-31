"""Given a non-empty sequence of characters s, return true if sequence is Binary, else return false.

Examples:

Input: s = "101"
Output: true
Explanation: Since string contains only '0' and '1', output is true.

Input: s = "75"
Output: false
Explanation: Since string contains digits other than '0' and '1', output is false."""


class Solution:
    def isBinary(self, s):
        return all(ch in '01' for ch in s)

# Example usage
sol = Solution()
print(sol.isBinary("101"))  # Output: True
print(sol.isBinary("75"))   # Output: False
print(sol.isBinary("001100"))  # Output: True
print(sol.isBinary("1234"))  # Output: False
