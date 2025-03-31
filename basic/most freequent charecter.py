"""Given a string s of lowercase alphabets. The task is to find the maximum occurring character in the string s. If more than one character occurs the maximum number of times then print the lexicographically smaller character.

Examples:

Input: s = "testsample"
Output: 'e'
Explanation: e is the character which is having the highest frequency.

Input: s = "output"
Output: 't'
Explanation:  t and u are the characters with the same frequency, but t is lexicographically smaller."""


class Solution:
    def getMaxOccurringChar(self, s):
        freq = {}  # Dictionary to store character frequencies

        # Count frequency of each character
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Find the character with maximum frequency and smallest lexicographically
        max_freq = max(freq.values())
        max_char = min([char for char in freq if freq[char] == max_freq])

        return max_char

# Example usage
sol = Solution()
print(sol.getMaxOccurringChar("testsample"))  # Output: 'e'
print(sol.getMaxOccurringChar("output"))      # Output: 't'
