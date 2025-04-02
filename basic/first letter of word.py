'''Given a string S, the task is to create a string with the first letter of every word in the string.
 

Example 1:

Input: 
S = "geeks for geeks"
Output: gfg

Example 2:

Input: 
S = "bad is good"
Output: big

Your Task:
You don't need to read input or print anything. Your task is to complete the function firstAlphabet() which takes string S as input parameter and returns a string that contains the first letter of every word in S.


Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)'''


class Solution:
    def firstAlphabet(self, S):
        return ''.join(word[0] for word in S.split())  # Extract first letter of each word

# Example usage:
sol = Solution()
print(sol.firstAlphabet("geeks for geeks"))  # Output: "gfg"
print(sol.firstAlphabet("bad is good"))  # Output: "big"
print(sol.firstAlphabet("hello world python"))  # Output: "hwp"
print(sol.firstAlphabet("open ai chat gpt"))  # Output: "oacg"
