'''Given two strings S1 and S2 as input, the task is to merge them alternatively i.e. the first character of S1 then the first character of S2 and so on till the strings end.
NOTE: Add the whole string if other string is empty.

Example 1:

Input:
S1 = "Hello" S2 = "Bye"
Output: HBeylelo
Explanation: The characters of both the 
given strings are arranged alternatlively.

â€‹Example 2:

Input: 
S1 = "abc", S2 = "def"
Output: adbecf
Explanation: The characters of both the
given strings are arranged alternatlively.
'''


class Solution:
    def mergeAlternately(self, S1, S2):
        result = []
        len1, len2 = len(S1), len(S2)
        
        # Merge characters alternately
        for i in range(min(len1, len2)):
            result.append(S1[i])  # Add character from S1
            result.append(S2[i])  # Add character from S2
        
        # Add remaining characters from the longer string
        result.append(S1[min(len1, len2):])
        result.append(S2[min(len1, len2):])

        return "".join(result)

# Example usage:
sol = Solution()
print(sol.mergeAlternately("Hello", "Bye"))  # Output: "HBeylelo"
print(sol.mergeAlternately("abc", "def"))  # Output: "adbecf"
print(sol.mergeAlternately("abcd", "pq"))  # Output: "apbqcd"
print(sol.mergeAlternately("x", "mnop"))  # Output: "xmnp"
