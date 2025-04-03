'''Given a string, check if all its characters are the same or not.

Example 1:

Input:
s = "geeks"
Output: False
Explanation: The string contains different
character 'g', 'e', 'k' and 's'.

Example 2:

Input: 
s = "gggg"
Output: True
Explanation: The string contains only one
character 'g'.


Your Task:
You don't need to read input or print anything. Your task is to complete the function check() which takes a string as input and returns True if all the characters in the string are the same. Else, it returns False.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).'''


class Solution:
    def check(self, s):
        return all(c == s[0] for c in s)  # Check if all characters are the same as the first one
    def check(self, s):
        return len(set(s)) == 1
# Example usage:
sol = Solution()
print(sol.check("geeks"))  # Output: False
print(sol.check("gggg"))   # Output: True
print(sol.check("aaaaa"))  # Output: True
print(sol.check("abc"))    # Output: False
print(sol.check("z"))      # Output: True (Only one character)

