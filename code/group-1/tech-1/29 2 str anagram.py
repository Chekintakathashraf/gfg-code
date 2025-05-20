# using sorting

def are_anagrams_sort(s1, s2):
    return sorted(s1) == sorted(s2)


#  Code (Using Frequency Count):

def are_anagrams_freq(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}

    for char in s1:
        freq[char] = freq.get(char, 0) + 1

    for char in s2:
        if char not in freq or freq[char] == 0:
            return False
        freq[char] -= 1

    return True

print(are_anagrams_sort("listen", "silent"))  # True
print(are_anagrams_sort("hello", "bello"))    # False

print(are_anagrams_freq("race", "care"))      # True
print(are_anagrams_freq("test", "tseta"))     # False

