'''Given two strings s1 and s2 in lowercase, the task is to make them anagrams. The only allowed operation is to remove a character from any string. Find the minimum number of characters to be deleted to make both the strings anagram. Two strings are called anagrams of each other if one of them can be converted into another by rearranging its letters.

Examples:

Input: s1 = "bcadeh", s2 = "hea"
Output: 3
Explanation: We need to remove b, c and d from s1.

Input: s1 = "cddgk", s2 = "gcd"
Output: 2
Explanation: We need to remove d and k from s1.'''


from collections import Counter

class Solution:
    def minDeletions(self, s1, s2):
        # Count frequency of characters in both strings
        count1 = Counter(s1)
        count2 = Counter(s2)
        
        # Initialize deletions counter
        deletions = 0
        
        # Set of all characters that appear in either s1 or s2
        all_chars = set(count1.keys()).union(set(count2.keys()))
        
        # For each character, calculate the difference in frequency
        for char in all_chars:
            deletions += abs(count1.get(char, 0) - count2.get(char, 0))
        
        return deletions

# Test cases
solution = Solution()
print(solution.minDeletions("bcadeh", "hea"))  # Output: 3
print(solution.minDeletions("cddgk", "gcd"))   # Output: 2


class Solution:
    def minDeletions(self, s1, s2):
        # Initialize frequency arrays for both strings
        freq1 = [0] * 26  # Frequency of characters in s1
        freq2 = [0] * 26  # Frequency of characters in s2
        
        # Count frequency of characters in s1
        for char in s1:
            freq1[ord(char) - ord('a')] += 1
        
        # Count frequency of characters in s2
        for char in s2:
            freq2[ord(char) - ord('a')] += 1
        
        # Calculate the number of deletions required
        deletions = 0
        for i in range(26):
            deletions += abs(freq1[i] - freq2[i])
        
        return deletions

# Test cases
solution = Solution()
print(solution.minDeletions("bcadeh", "hea"))  # Output: 3
print(solution.minDeletions("cddgk", "gcd"))   # Output: 2
