"""You are given a string s, consisting of lowercase alphabets. Your task is to remove consecutive duplicate characters from the string. 

Example:

Input: s = "aabb"
Output:  "ab" 
Explanation: 
The character 'a' at index 2 is the same as 'a' at index 1, so it is removed.
Similarly, the character 'b' at index 4 is the same as 'b' at index 3, so it is removed.
The final string is "ab".

Input:s = "aabaa"
Output: "aba"
Explanation: 
The character 'a' at index 2 is the same as 'a' at index 1, so it is removed.
The character 'a' at index 5 is the same as 'a' at index 4, so it is removed.
The final string is "aba".

Input: s = "abcddcba"
Output: "abcdcba"
Explanation: 
The character 'd' at index 5 is the same as 'd' at index 4, so it is removed.
No other consecutive duplicates exist.
The final string is "abcdcba"."""


class Solution:
    def removeConsecutiveDuplicates(self, s):
        result = [s[0]]  # Initialize with first character
        
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:  # Add only if different from previous character
                result.append(s[i])
        
        return "".join(result)  # Convert list back to string

# Test cases
sol = Solution()
print(sol.removeConsecutiveDuplicates("aabb"))      # Output: "ab"
print(sol.removeConsecutiveDuplicates("aabaa"))     # Output: "aba"
print(sol.removeConsecutiveDuplicates("abcddcba"))  # Output: "abcdcba"
print(sol.removeConsecutiveDuplicates("aaaa"))      # Output: "a"
print(sol.removeConsecutiveDuplicates("ab"))        # Output: "ab"
print(sol.removeConsecutiveDuplicates("a"))         # Output: "a"
