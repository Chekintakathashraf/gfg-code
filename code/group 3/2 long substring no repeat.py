"""Given a string s, find the length of the longest substring that contains only unique characters (no repeating characters).

A substring is a contiguous block of characters inside the string."""


def length_of_longest_substring(s: str) -> int:
    char_set = set()
    start = 0
    max_length = 0

    for end in range(len(s)):
        # Shrink window if duplicate found
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1

        char_set.add(s[end])
        max_length = max(max_length, end - start + 1)

    return max_length

# Test examples
print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1
print(length_of_longest_substring("pwwkew"))    # 3
