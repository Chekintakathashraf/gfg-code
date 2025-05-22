"""Given two strings s and t, write a function to determine if t is an anagram of s.

An anagram means the strings contain the same characters with the same frequency, but in any order."""


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for ch in s:
        count_s[ch] = count_s.get(ch, 0) + 1

    for ch in t:
        count_t[ch] = count_t.get(ch, 0) + 1

    return count_s == count_t

# Test
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram("aabbcc", "abcabc"))    # True

