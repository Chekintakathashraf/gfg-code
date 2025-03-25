"""Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']', verify the validity of the arrangement.
An input string is valid if:

         1. Open brackets must be closed by the same type of brackets.
         2. Open brackets must be closed in the correct order.

Examples :

Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.

Input: s = "[()()]{}"
Output: true
Explanation: All the brackets are well-formed.

Input: s = "([]"
Output: False
Explanation: The expression is not balanced as there is a missing ')' at the end.

Input: s = "([{]})"
Output: False
Explanation: The expression is not balanced as there is a closing ']' before the closing '}'."""

def is_valid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}  # Matching pairs

    for char in s:
        if char in bracket_map:  # If closing bracket
            top = stack.pop() if stack else '#'  # Pop or use dummy value
            if bracket_map[char] != top:  
                return False  # Mismatch
        else:
            stack.append(char)  # Push opening bracket

    return not stack  # Valid if stack is empty

# Test Cases
print(is_valid("[{()}]"))  # Output: True
print(is_valid("[()()]{}"))  # Output: True
print(is_valid("([]"))  # Output: False
print(is_valid("([{]})"))  # Output: False
