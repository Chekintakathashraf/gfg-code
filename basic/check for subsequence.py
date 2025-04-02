'''Given two strings A and B, find if A is a subsequence of B.

Example 1:

Input:
A = AXY 
B = YADXCP
Output: 0 
Explanation: A is not a subsequence of B
as 'Y' appears before 'A'.

 

Example 2:

Input:
A = gksrek
B = geeksforgeeks
Output: 1
Explanation: A is a subsequence of B.

 

Your Task:  
You dont need to read input or print anything. Complete the function isSubSequence() which takes A and B as input parameters and returns a boolean value denoting if A is a subsequence of B or not. 

 

Expected Time Complexity: O(N) where N is length of string B.
Expected Auxiliary Space: O(1)'''

class Solution:
    # Function to check if A is a subsequence of B
    def isSubSequence(self, A, B):
        i, j = 0, 0  # i for A, j for B
        
        while j < len(B) and i < len(A):
            if A[i] == B[j]:  # If characters match, move to next character in A
                i += 1
            j += 1  # Always move to the next character in B
        
        return i == len(A)  # If i reached end of A, A is a subsequence of B

# Example usage:
sol = Solution()
print(sol.isSubSequence("AXY", "YADXCP"))  # Output: False (0)
print(sol.isSubSequence("gksrek", "geeksforgeeks"))  # Output: True (1)
