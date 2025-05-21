"""Given a string s, find the length of the longest substring without repeating characters."""

def length_of_longest_substring(s):
    char_index = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        c = s[end]
        if c in char_index and char_index[c] >= start:
            start = char_index[c] + 1
        char_index[c] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# Test cases
print(length_of_longest_substring("abcabcbb"))  # Output: 3
print(length_of_longest_substring("bbbbb"))     # Output: 1
print(length_of_longest_substring("pwwkew"))    # Output: 3
print(length_of_longest_substring(""))          # Output: 0

