"""You are given a string s and an integer k.

Return the maximum number of vowels in any substring of length k."""

def max_vowels(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    max_vowels = 0

    # Initial window
    for i in range(k):
        if s[i] in vowels:
            count += 1
    max_vowels = count

    # Slide the window
    for i in range(k, len(s)):
        if s[i] in vowels:
            count += 1
        if s[i - k] in vowels:
            count -= 1
        max_vowels = max(max_vowels, count)

    return max_vowels

# Test examples
print(max_vowels("abciiidef", 3))  # 3
print(max_vowels("aeiou", 2))      # 2
print(max_vowels("leetcode", 3))   # 2

