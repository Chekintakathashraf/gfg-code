"""You are given a string S, the task is to reverse the string using stack.

Example 1:

Input: S="GeeksforGeeks"
Output: skeeGrofskeeG

Example 2:

Input: S="Geek"
Output: keeG

Your Task:
You don't need to read input or print anything. Your task is to complete the function reverse() which takes the string S as an input parameter and returns the reversed string.

Constraints:
1 ≤ length of the string ≤ 100"""

def reverse(S):
    stack = list(S)  # Step 1: Push all characters into stack
    result = ""  
    while stack:  # Step 2: Pop characters from stack
        result += stack.pop()
    return result

# Test cases
print(reverse("GeeksforGeeks"))  # Output: "skeeGrofskeeG"
print(reverse("Geek"))           # Output: "keeG"
