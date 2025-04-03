'''Given a alphanumeric string S, extract maximum numeric value from S.

Example 1:

Input:
S = 100klh564abc365bg
Output: 564
Explanation: Maximum numeric value 
among 100, 564 and 365 is 564.

Example 2:

Input:
S = abcdefg
Output: -1
Explanation: Return -1 if no numeric 
value is present. 


Your Task:  
You dont need to read input or print anything. Complete the function extractMaximum() which takes the string S as input parameters and returns the maximum numeric value. If it is not present in S, return -1.

 

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)'''


class Solution:
    def extractMaximum(self, S):
        max_num = -1  # Default if no number is found
        num = ""  # To store the current number

        for ch in S:
            if ch.isdigit():
                num += ch  # Build number if character is digit
            else:
                if num:  
                    max_num = max(max_num, int(num))  # Compare with max found
                    num = ""  # Reset for next number
        
        if num:  # Check if last number is the max
            max_num = max(max_num, int(num))

        return max_num

# Example usage:
sol = Solution()
print(sol.extractMaximum("100klh564abc365bg"))  # Output: 564
print(sol.extractMaximum("abcdefg"))           # Output: -1
print(sol.extractMaximum("a12b34c99"))         # Output: 99
