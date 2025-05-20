
""" Summary of This Pattern:

    If you want the first unique → use dict + count

    If you want the first repeat → use set while iterating"""



def first_repeating_char(s: str) -> str:
    seen = set()
    for char in s:
        if char in seen:
            return char  # first one that repeats
        seen.add(char)
    return "None"


print(first_repeating_char("programming"))  # r
print(first_repeating_char("abcdef"))       # None
print(first_repeating_char("abca"))         # a
print(first_repeating_char("aabb"))         # a


