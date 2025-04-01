'''Given two strings s1 and s2. Modify both the strings such that all the common characters of s1 and s2 are to be removed and the uncommon characters of s1 and s2 are to be concatenated.
Note: If all characters are removed print -1.

Example 1:

Input:
s1 = aacdb
s2 = gafd
Output: cbgf
Explanation: The common characters of s1
and s2 are: a, d. The uncommon characters
of s1 and s2 are c, b, g and f. Thus the
modified string with uncommon characters
concatenated is cbgf.

Example 2:

Input:
s1 = abcs
s2 = cxzca
Output: bsxz
Explanation: The common characters of s1
and s2 are: a,c. The uncommon characters
of s1 and s2 are b,s,x and z. Thus the
modified string with uncommon characters
concatenated is bsxz.

Your Task:
The task is to complete the function concatenatedString() which removes the common characters, concatenates, and returns the string. If all characters are removed then return -1.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Number of distinct characters).
Note: N = |Length of Strings|

'''


class Solution:
    def concatenatedString(self, s1: str, s2: str) -> str:
        # Convert both strings to sets to get common characters
        set_s1 = set(s1)
        set_s2 = set(s2)
        
        # Find common characters
        common_chars = set_s1.intersection(set_s2)
        
        # Create new strings by removing common characters
        result_s1 = ''.join([char for char in s1 if char not in common_chars])
        result_s2 = ''.join([char for char in s2 if char not in common_chars])
        
        # Concatenate the results
        result = result_s1 + result_s2
        
        # If no characters left, return -1
        if result == "":
            return "-1"
        
        return result


# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.concatenatedString("aacdb", "gafd"))  # Output: "cbgf"
    print(solution.concatenatedString("abcs", "cxzca"))  # Output: "bsxz"
