"""Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, "act" and "tac" are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.

Note: You can assume both the strings s1 & s2 are non-empty.

Examples :

Input: s1 = "geeks", s2 = "kseeg"
Output: true
Explanation: Both the string have same characters with same frequency. So, they are anagrams.

Input: s1 = "allergy", s2 = "allergic"
Output: false
Explanation: Characters in both the strings are not same, so they are not anagrams.

Input: s1 = "g", s2 = "g"
Output: true
Explanation: Character in both the strings are same, so they are anagrams."""

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False  # Different lengths cannot be anagrams

    freq1, freq2 = {}, {}

    # Count frequency of each character
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1
    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1

    return freq1 == freq2  # Compare both frequency dictionaries

# Test Cases
print(are_anagrams("geeks", "kseeg"))  # Output: True
print(are_anagrams("allergy", "allergic"))  # Output: False
print(are_anagrams("g", "g"))  # Output: True
