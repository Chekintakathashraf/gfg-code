'''Given a string S, remove all consonants and print the modified string that contains vowels only.

Example 1:

Input
S = "abEkipo"
Output
aEio
Explanation : a, E, i, o are only vowels in the string.

Example 2:

Input
S = "rrty"
Output
No Vowel
Explanation: There are no vowels.

Your Task: You don't need to read input or print anything.Your task is to complete the function removeConsonants() which takes a string as input parameters, and returns the modified string that contains vowels only. If there is no vowel present in the string S, then return "No Vowel".

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).'''

class Solution:
    def removeConsonants(self, S):
        vowels = "aeiouAEIOU"
        result = "".join([char for char in S if char in vowels])
        return result if result else "No Vowel"

# Example usage
sol = Solution()
print(sol.removeConsonants("abEkipo"))  # Output: aEio
print(sol.removeConsonants("rrty"))     # Output: No Vowel
