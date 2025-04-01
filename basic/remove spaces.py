'''Given a string s. Your task is to remove spaces from it. 

Examples:

Input: s = "geeks  for geeks"
Output: "geeksforgeeks"
Explanation: All the spaces have been removed.

Input: s = "    g f g"
Output: "gfg"
Explanation: All the spaces including the leading ones have been removed.
'''


class Solution:
    def removeSpaces(self, s: str) -> str:
        return s.replace(" ", "")
    

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.removeSpaces("geeks  for geeks"))  # Output: "geeksforgeeks"
    print(solution.removeSpaces("    g f g"))        # Output: "gfg"
