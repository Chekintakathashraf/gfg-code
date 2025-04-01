"""Given a string s. The task is to convert string characters to lowercase.

Examples:

Input: s = "ABCddE"
Output: "abcdde"
Explanation: A, B, C and E are converted to a, b, c and e thus all uppercase characters of the string converted to lowercase letter.

Input: s = "LMNOppQQ"
Output: "lmnoppqq"
Explanation: L, M, N, O, and Q are converted to l, m, n, o and q thus all uppercase characters of the string converted to lowercase letter."""


class Solution:
    def toLower(self, s: str) -> str:
        return s.lower()

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s = "ABCddE"
    print(solution.toLower(s))  # Output: "abcdde"
    
    # Test Case 2
    s = "LMNOppQQ"
    print(solution.toLower(s))  # Output: "lmnoppqq"
    
    # Test Case 3
    s = "hello"
    print(solution.toLower(s))  # Output: "hello" (unchanged)
    
    # Test Case 4
    s = "PYTHON123"
    print(solution.toLower(s))  # Output: "python123" (numbers remain unchanged)
