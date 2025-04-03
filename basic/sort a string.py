'''Given a string consisting of lowercase letters, arrange all its letters in ascending order. 

Example 1:

Input:
S = "edcab"
Output: "abcde"
Explanation: characters are in ascending
order in "abcde".

Example 2:

Input:
S = "xzy"
Output: "xyz"
Explanation: characters are in ascending
order in "xyz".



Your Task:  
You don't need to read input or print anything. Your task is to complete the function sort() which takes the string as inputs and returns the modified string.

Expected Time Complexity: O(|S| * log |S|)
Expected Auxiliary Space: O(1)'''


class Solution:
    def sort(self, S):
        return "".join(sorted(S))  # Sort characters and join them back into a string

# Example usage:
sol = Solution()
print(sol.sort("edcab"))  # Output: "abcde"
print(sol.sort("xzy"))    # Output: "xyz"
print(sol.sort("hello"))  # Output: "ehllo"
print(sol.sort("geeks"))  # Output: "eegks"
