#Step 1: Count frequency of each character

def most_frequent_char(s: str) -> str:
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

#Step 2: Find the character with the highest count

    max_count = 0
    result_char = ""
    for char in freq:
        if freq[char] > max_count:
            max_count = freq[char]
            result_char = char
    return result_char


print(most_frequent_char("aabbbccde"))   # b
print(most_frequent_char("xyzxyzz"))     # z
print(most_frequent_char("aaaaa"))       # a
print(most_frequent_char(""))            # "" (can handle empty too)
