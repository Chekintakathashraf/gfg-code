'''Given a string s, convert the first letter of each word in the string to uppercase. 

Examples:

Input: s = "gEEKs"
Output: "Geeks"

Input: s = "i love programming"
Output: "I Love Programming"'''


class Solution:
    def capitalizeWords(self, s):
        return s.title()  # Converts the first letter of each word to uppercase

# Example usage:
sol = Solution()
print(sol.capitalizeWords("gEEKs"))  # Output: "Geeks"
print(sol.capitalizeWords("i love programming"))  # Output: "I Love Programming"
print(sol.capitalizeWords("hello world"))  # Output: "Hello World"
print(sol.capitalizeWords("PYTHON is FUN"))  # Output: "Python Is Fun"
