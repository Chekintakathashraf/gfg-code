def longest_unique_substring(s):
    seen = set()
    start_index = 0
    max_length = 0
    max_start_index = 0  # to remember where the best substring starts

    for end in range(len(s)):
        while s[end] in seen:
            seen.remove(s[start_index])
            start_index += 1

        seen.add(s[end])

        if end - start_index + 1 > max_length:
            max_length = end - start_index + 1
            max_start_index = start_index

    return max_length, s[max_start_index:max_start_index + max_length]


print(longest_unique_substring("abcabcbb"))  # Output: (3, 'abc')
print(longest_unique_substring("abba"))      # Output: (2, 'ab' or 'ba')
print(longest_unique_substring("pwwkew"))    # Output: (3, 'wke')
