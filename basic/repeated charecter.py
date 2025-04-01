"""Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

NOTE - If there are no repeating characters return '#'.

Example 1:

Input:
S = "geeksforgeeks"
Output: g
Explanation: g, e, k and s are the repeating
characters. Out of these, g occurs first. 

Example 2:

Input: 
S = "abcde"
Output: -1
Explanation: No repeating character present. (You need to return '#')


Your Task:
You don't need to read input or print anything. Your task is to complete the function firstRep() which takes the string S as input and returns the the first repeating character in the string. In case there's no repeating character present, return '#'.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1)."""


class Solution:
    def firstRep(self, S):
        char_count = {}  # Dictionary to store character frequency and first occurrence index
        
        for i, char in enumerate(S):
            if char in char_count:
                char_count[char][0] += 1  # Increment frequency
            else:
                char_count[char] = [1, i]  # Store frequency and index
        
        # Find the first character that appears more than once
        first_repeating = '#'
        min_index = float('inf')

        for char, (count, index) in char_count.items():
            if count > 1 and index < min_index:
                min_index = index
                first_repeating = char
        
        return first_repeating

# Driver Code to test the function
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    print(solution.firstRep("geeksforgeeks"))  # Output: g
    
    # Test Case 2
    print(solution.firstRep("abcde"))  # Output: #

    # Test Case 3
    print(solution.firstRep("abacbc"))  # Output: a
