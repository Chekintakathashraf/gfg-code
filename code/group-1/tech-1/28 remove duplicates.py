def remove_duplicates(s):
    seen = set()
    result = []

    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)

print(remove_duplicates("programming"))  # "progamin"
print(remove_duplicates("banana"))       # "ban"
print(remove_duplicates("aabbcc"))       # "abc"
print(remove_duplicates("abcd"))         # "abcd"

