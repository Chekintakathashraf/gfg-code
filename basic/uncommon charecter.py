"""You are given two strings s1 and s2. Your task is to identify the characters that appear in either string but not in both (i.e., characters that are unique to one of the strings). Return the result as a sorted string.

Examples:

Input: s1 = "geeksforgeeks", s2 = "geeksquiz"
Output: "fioqruz"
Explanation: The characters 'f', 'i', 'o', 'q', 'r', 'u', and 'z' are present in either s1 or s2, but not in both.

Input: s1 = "characters", s2 = "alphabets"
Output: "bclpr"
Explanation: The characters 'b', 'c', 'l', 'p', and 'r' are present in either s1 or s2, but not in both.

Input: s1 = "rome", s2 = "more"
Output: ""
Explanation: Both strings contain the same characters, so there are no unique characters. The output is an empty string."""

class Solution:
    def uniqueCharacters(self, s1, s2):
        # Convert strings to sets to find unique characters
        set1 = set(s1)
        set2 = set(s2)
        
        # Find symmetric difference to get unique characters from both strings
        unique_chars = set1 ^ set2
        
        # Sort the result and return as a string
        return ''.join(sorted(unique_chars))

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s1 = "geeksforgeeks"
    s2 = "geeksquiz"
    print(solution.uniqueCharacters(s1, s2))  # Output: "fioqruz"
    
    # Test Case 2
    s1 = "characters"
    s2 = "alphabets"
    print(solution.uniqueCharacters(s1, s2))  # Output: "bclpr"
    
    # Test Case 3
    s1 = "rome"
    s2 = "more"
    print(solution.uniqueCharacters(s1, s2))  # Output: ""


