def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "ohllea"))    # False
print(is_anagram("test", "ttew"))      # False
