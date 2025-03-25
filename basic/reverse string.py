'''You are given a string s, and your task is to reverse the string.

Examples:

Input: s = "Geeks"
Output: "skeeG"

Input: s = "for"
Output: "rof"

Input: s = "a"
Output: "a" '''


# Method 1: Using slicing
def reverse_string_slice(s):
    return s[::-1]  # Pythonic way

# Method 2: Using reversed() and join()
def reverse_string_reversed(s):
    return "".join(reversed(s))  # Converts reversed iterator to string

# Method 3: Using a loop
def reverse_string_loop(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s  # Prepend character
    return reversed_s

# Test Cases
test_cases = ["Geeks", "for", "a"]

for s in test_cases:
    print(f"Original: {s}")
    print(f"Slice Method: {reverse_string_slice(s)}")
    print(f"Reversed Function: {reverse_string_reversed(s)}")
    print(f"Loop Method: {reverse_string_loop(s)}")
    print("-" * 30)
