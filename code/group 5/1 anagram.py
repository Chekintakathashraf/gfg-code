
"""Given two strings s1 and s2, check if they are anagrams of each other.

A string is an anagram of another if it contains the same characters with the same frequency, just arranged differently."""




def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

# ✅ Test Cases
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "bello"))    # False
print(are_anagrams("aacc", "ccac"))      # False
print(are_anagrams("abc", "cab"))        # True
