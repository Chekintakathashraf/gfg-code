#Option 1: Using Sorting

def is_anagram(a, b):
    return sorted(a) == sorted(b)

#  Using Frequency Count (Dict)

def is_anagram(a, b):
    if len(a) != len(b):
        return False

    freq_a = {}
    freq_b = {}

    for char in a:
        freq_a[char] = freq_a.get(char, 0) + 1

    for char in b:
        freq_b[char] = freq_b.get(char, 0) + 1

    return freq_a == freq_b

print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "bello"))     # False
print(is_anagram("race", "care"))       # True
print(is_anagram("a", "aa"))            # False
