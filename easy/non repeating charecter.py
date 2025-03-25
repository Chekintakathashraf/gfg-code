"""Given a string s consisting of lowercase English Letters. Return the first non-repeating character in s.
If there is no non-repeating character, return '$'.
Note: When you return '$' driver code will output -1.

Examples:

Input: s = "geeksforgeeks"
Output: 'f'
Explanation: In the given string, 'f' is the first character in the string which does not repeat.

Input: s = "racecar"
Output: 'e'
Explanation: In the given string, 'e' is the only character in the string which does not repeat.

Input: s = "aabbccc"
Output: -1
Explanation: All the characters in the given string are repeating."""

def first_non_repeating_char(s):
    char_count = {}  # Dictionary to store character frequencies

    # First pass: Count occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Second pass: Find the first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char

    return '$'  # If no unique character exists

# Test cases
print(first_non_repeating_char("geeksforgeeks"))  # Output: 'f'
print(first_non_repeating_char("racecar"))        # Output: 'e'
print(first_non_repeating_char("aabbccc"))        # Output: '$' (driver code prints -1)
