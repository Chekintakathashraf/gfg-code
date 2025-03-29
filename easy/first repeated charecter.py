"""Given a string s. The task is to find the first repeated character in it. We need to find the character that occurs more than once and whose index of second occurrence is smallest. s contains only lowercase letters.

Examples :

Input: s ="geeksforgeeks"
Output: "e"
Explanation: 'e' repeats at third position.

Input: s ="hellogeeks"
Output: "l"
Explanation: 'l' repeats at fourth position.

Input: s ="abc"
Output: "-1"
Explanation: There is no repeated character."""


class Solution:
    def firstRepeatedChar(self, s):
        seen = set()  # Set to store characters
        
        for char in s:
            if char in seen:  # If character is already seen, return it
                return char
            seen.add(char)  # Add character to set
        
        return "-1"  # No repeated character found

# Test cases
sol = Solution()
print(sol.firstRepeatedChar("geeksforgeeks"))  # Output: "e"
print(sol.firstRepeatedChar("hellogeeks"))     # Output: "l"
print(sol.firstRepeatedChar("abc"))            # Output: "-1"
