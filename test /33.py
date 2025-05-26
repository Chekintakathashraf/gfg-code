def longest_unique_substring_length(s):
    seen = set()
    start_index = 0
    max_length = 0

    for end in range(len(s)):
        while s[end] in seen:
            seen.remove(s[start_index])
            start_index += 1

        seen.add(s[end])
        max_length = max(max_length, end - start_index + 1)

    return max_length

print(longest_unique_substring_length("abcabcbb"))  # Output: 3
print(longest_unique_substring_length("abba"))      # Output: 2
print(longest_unique_substring_length("pwwkew"))    # Output: 3
