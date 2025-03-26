"""Given two strings s1 and s2, check if these two strings are isomorphic to each other.

If the characters in s1 can be changed to get s2, then two strings, s1 and s2, are isomorphic. A character must be completely swapped out for another character while maintaining the order of the characters. A character may map to itself, but no two characters may map to the same character.

Examples:

Input: s1 = "aab", s2 = "xxy"
Output: true
Explanation: There are two different characters in aab and xxy, i.e a and b with frequency 2 and 1 respectively.

Input: s1 = "aab", s2 = "xyz"
Output: false
Explanation:  There are two different characters in aab but there are three different charactersin xyz. So there won't be one to one mapping between s1and s2.

Input: s1 = "aac", s2 = "xyz"
Output: false
Explanation: There are two different characters in aab but there are three different charactersin xyz. So there won't be one to one mapping between s1and s2."""


def are_isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False  # Strings must be of the same length

    mapping_s1_to_s2 = {}
    mapping_s2_to_s1 = {}

    for char1, char2 in zip(s1, s2):
        if (char1 in mapping_s1_to_s2 and mapping_s1_to_s2[char1] != char2) or \
           (char2 in mapping_s2_to_s1 and mapping_s2_to_s1[char2] != char1):
            return False
        
        mapping_s1_to_s2[char1] = char2
        mapping_s2_to_s1[char2] = char1

    return True

# 🔹 Test Cases
print(are_isomorphic("aab", "xxy"))  # ✅ True
print(are_isomorphic("aab", "xyz"))  # ❌ False
print(are_isomorphic("aac", "xyz"))  # ❌ False
print(are_isomorphic("egg", "add"))  # ✅ True
print(are_isomorphic("foo", "bar"))  # ❌ False
