"""Given a string s consisting of only '0's and '1's,  find the last index of the '1' present.

Note: If '1' is not present, return "-1"

Examples:

Input: s = 00001
Output: 4
Explanation: Last index of  1 in given string is 4.

Input: s = 0
Output: -1
Explanation: Since, 1 is not present, so output is -1.

Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)"""

class Solution:
    def lastIndexOfOne(self, s):
        # Traverse the string in reverse order to find the last occurrence of '1'
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                return i
        # If no '1' is found, return -1
        return -1

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s = "00001"
    print(solution.lastIndexOfOne(s))  # Output: 4
    
    # Test Case 2
    s = "0"
    print(solution.lastIndexOfOne(s))  # Output: -1
    
    # Test Case 3
    s = "101010"
    print(solution.lastIndexOfOne(s))  # Output: 5
