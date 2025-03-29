"""Given a string s1 and another string s2. Find the minimum index of the character in s1 that is also present in s2.

Examples :

Input: s1 = "geeksforgeeks", s2 = "set"
Output: 1
Explanation: e is the character which is present in given s1 "geeksforgeeks" and is also present in s2 "set". Minimum index of e is 1. 

Input: s1 = "adcffaet", s2 = "onkl"
Output: -1
Explanation: There are none of the characters which is common in s1 and s2."""



class Solution:
    def minIndexChar(self, s1, s2):
        char_set = set(s2)  # Convert s2 to a set for quick lookup
        
        for i, char in enumerate(s1):  # Iterate over s1
            if char in char_set:  # If char is present in s2
                return i  # Return the first found index
        
        return -1  # No common character found

# Test cases
sol = Solution()
print(sol.minIndexChar("geeksforgeeks", "set"))  # Output: 1
print(sol.minIndexChar("adcffaet", "onkl"))     # Output: -1
