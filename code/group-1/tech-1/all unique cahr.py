def find_uniques(s):
    freq = {}
    
    # Step 1: Count characters
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Step 2: Collect characters with frequency 1
    result = []
    for char in s:
        if freq[char] == 1:
            result.append(char)
    
    return result

print(find_uniques("success"))       # ['u', 'e']
print(find_uniques("programming"))   # ['p', 'o', 'a', 'i', 'n']
print(find_uniques("aabbccdd"))      # []
print(find_uniques("abacbd"))        # ['c']

