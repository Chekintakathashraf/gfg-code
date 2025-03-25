"""Given two strings s1 and s2. Return true if the string s2 can be obtained by rotating (in any direction) string s1 by exactly 2 places, otherwise, false.

Note: Both rotations should be performed in same direction chosen initially.

Examples:

Input: s1 = "amazon", s2 = "azonam"
Output: true
Explanation: "amazon" can be rotated anti-clockwise by two places, which will make it as "azonam".

Input: s1 = "geeksforgeeks", s2 = "geeksgeeksfor"
Output: false
Explanation: If we rotate "geeksforgeeks" by two place in any direction, we won't get "geeksgeeksfor".

Input: s1 = "ab", s2 = "ab"
Output: true
Explanation: If we rotate "ab" by two place in any direction, we always get "ab"."""


def isRotatedByTwo(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) < 2:  # Edge case: If length < 2, rotation doesn't change the string
        return s1 == s2

    left_rot = s1[2:] + s1[:2]   # Left rotation
    right_rot = s1[-2:] + s1[:-2] # Right rotation

    return s2 == left_rot or s2 == right_rot

# Example Usage:
print(isRotatedByTwo("amazon", "azonam"))  # Output: True
print(isRotatedByTwo("geeksforgeeks", "geeksgeeksfor"))  # Output: False
print(isRotatedByTwo("ab", "ab"))  # Output: True

