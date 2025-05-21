"""Given a string s, find the length of the longest substring without repeating characters."""

def length_of_longest_substring(s):
    char_set = set()
    start = max_length = 0

    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_length = max(max_length, end - start + 1)

    return max_length

# Test
print(length_of_longest_substring("abcabcbb"))  # Output: 3
print(length_of_longest_substring("bbbbb"))     # Output: 1
print(length_of_longest_substring("pwwkew"))    # Output: 3

