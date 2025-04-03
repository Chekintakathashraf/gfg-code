'''iven a string str containing only lowercase letters, generate a string with the same letters, but in uppercase.

Example 1:

Input:
str = "geeks"
Output: GEEKS

Example 2:

Input:
str = "geeksforgeeks"
Output: GEEKSFORGEEKS

Your Task:
You don't need to read input or print anything. Your task is to complete the function to_upper() which takes the string str as an argument and returns the resultant string.

Expected Time Complexity: O(length of the string).
Expected Auxiliary Space: O(1).'''

class Solution:
    def to_upper(self, str):
        return str.upper()  # Convert to uppercase

# Example usage
sol = Solution()
print(sol.to_upper("geeks"))  # Output: GEEKS
print(sol.to_upper("geeksforgeeks"))  # Output: GEEKSFORGEEKS
