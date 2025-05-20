"""Given a string s, find the length of the longest substring without repeating characters."""

def length_of_longest_substring(s):
    char_set = set()
    start = 0
    max_len = 0

    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_len = max(max_len, end - start + 1)

    return max_len

# Test examples
print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1
print(length_of_longest_substring("pwwkew"))    # 3


