def most_frequent_char(s):
    freq = {}
    max_freq = 0
    max_char = None

    for char in s:
        freq[char] = freq.get(char, 0) + 1
        
        # Update max freq and char if needed
        if freq[char] > max_freq:
            max_freq = freq[char]
            max_char = char

    return max_char

print(most_frequent_char("success"))  # Output: 's'
print(most_frequent_char("banana"))   # Output: 'a'
print(most_frequent_char("abcabc"))   # Output: 'a'

