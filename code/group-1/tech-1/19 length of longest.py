def length_of_longest_substring(s):
    start = 0
    max_length = 0
    seen = {}

    for end in range(len(s)):
        char = s[end]

        if char in seen and seen[char] >= start:
            start = seen[char] + 1  # move start pointer after last occurrence

        seen[char] = end  # update last index of char
        max_length = max(max_length, end - start + 1)

    return max_length

print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1
print(length_of_longest_substring("pwwkew"))    # 3
