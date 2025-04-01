"""Given a string s , return reverse of the string as output.

Example 1:

Input: 
s = "GeeksforGeeks"
Output: "skeeGrofskeeG" 
Explanation: Reverse string of "GeeksforGeeks" will be "skeeGrofskeeG"

Example 2:

Input: 
s = "ReversE"
Output: 'EsreveR'
Explanation: Reverse string of "ReversE" will be 'EsreveR'"""

class Solution:
    def reverseString(self, s: str) -> str:
        return s[::-1]  # Reverse using slicing

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.reverseString("GeeksforGeeks"))  # Output: "skeeGrofskeeG"
    print(solution.reverseString("ReversE"))       # Output: "EsreveR"
