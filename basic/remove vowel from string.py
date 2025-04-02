'''Given a string s. Your task is to remove the vowels from the string.

Examples:

Input: s = "welcome to geeksforgeeks"
Output: "wlcm t gksfrgks"
Explanation: Vowels were ignored only consonents were retuherned in the same order.

Input: s = "what is your name ?"
Output: wht s yr nm ?
'''


class Solution:
    def removeVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}  # Set of vowels
        return ''.join([char for char in s if char not in vowels])  # Filter out vowels

# Example usage:
sol = Solution()
print(sol.removeVowels("welcome to geeksforgeeks"))  # Output: "wlcm t gksfrgks"
print(sol.removeVowels("what is your name ?"))  # Output: "wht s yr nm ?"
print(sol.removeVowels("HELLO WORLD"))  # Output: "HLL WRLD"
print(sol.removeVowels("aeiouAEIOU"))  # Output: ""
