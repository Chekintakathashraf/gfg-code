"""You are given a string s containing lowercase English letters. You will be asked several queries, where each query gives a range [l, r] and a character c. Your task is to return how many times character c appears between index l and r (inclusive) efficiently."""


def build_prefix_frequency(s):
    n = len(s)
    prefix = [[0] * 26 for _ in range(n)]
    
    for i in range(n):
        if i > 0:
            prefix[i] = prefix[i-1][:]
        prefix[i][ord(s[i]) - ord('a')] += 1
    return prefix

def count_char_in_range(prefix, l, r, c):
    char_index = ord(c) - ord('a')
    if l == 0:
        return prefix[r][char_index]
    return prefix[r][char_index] - prefix[l - 1][char_index]

# Example usage:
s = "abacaba"
queries = [(0, 6, 'a'), (2, 4, 'b'), (1, 5, 'c')]

prefix = build_prefix_frequency(s)
for l, r, c in queries:
    print(count_char_in_range(prefix, l, r, c))  # Output: 4, 1, 1
