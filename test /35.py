def max_vowels_in_substring(s, k):
    vowels = set('aeiou')
    max_vowels = 0
    current_count = 0

    # First window of size k
    for i in range(k):
        if s[i] in vowels:
            current_count += 1
    max_vowels = current_count

    # Slide the window through the string
    for i in range(k, len(s)):
        if s[i - k] in vowels:
            current_count -= 1
        if s[i] in vowels:
            current_count += 1
        max_vowels = max(max_vowels, current_count)

    return max_vowels

print(max_vowels_in_substring("abciiidef", 3))  # Output: 3 (substring = "iii")
print(max_vowels_in_substring("aeiou", 2))      # Output: 2 (any 2-letter window)
print(max_vowels_in_substring("leetcode", 3))   # Output: 2 (substring = "eet")
