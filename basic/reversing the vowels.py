'''Given a string consisting of lowercase English alphabets, reverse only the vowels present in it and print the resulting string.

Examples:

Input: s = "geeksforgeeks"
Output: "geeksforgeeks"
Explanation: The vowels are: e, e, o, e, e. Reverse of these is also e, e, o, e, e.

Input: s = "practice"
Output: "prectica"
Explanation: The vowels are a, i, e. Reverse of these is e, i, a.

Input: s = "bcdfg"
Output: "bcdfg"
Explanation: There are no vowels in s.'''


class Solution:
    def reverseVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels (lowercase)
        s = list(s)  # Convert string to a list for easy swapping
        left, right = 0, len(s) - 1  # Two-pointer approach

        while left < right:
            if s[left] not in vowels:
                left += 1  # Move left pointer if not a vowel
            elif s[right] not in vowels:
                right -= 1  # Move right pointer if not a vowel
            else:
                s[left], s[right] = s[right], s[left]  # Swap vowels
                left += 1
                right -= 1

        return ''.join(s)  # Convert list back to string

# Example usage:
sol = Solution()
print(sol.reverseVowels("geeksforgeeks"))  # Output: "geeksforgeeks"
print(sol.reverseVowels("practice"))  # Output: "prectica"
print(sol.reverseVowels("bcdfg"))  # Output: "bcdfg"
print(sol.reverseVowels("hello"))  # Output: "holle"
