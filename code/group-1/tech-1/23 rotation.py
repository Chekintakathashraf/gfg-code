def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    combined = s1 + s1
    return s2 in combined

print(is_rotation("abcd", "cdab"))         # True
print(is_rotation("abcd", "acbd"))         # False
print(is_rotation("waterbottle", "erbottlewat"))  # True
print(is_rotation("abc", "cab"))           # True

