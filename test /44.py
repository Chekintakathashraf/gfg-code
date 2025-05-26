def build_char_prefix(s):
 
    freeq_prefix = {}

    for ch in set(s):  # only unique characters
        freeq_prefix[ch] = [0] * len(s)

    for i in range(len(s)):
        current = s[i]
        for ch in freeq_prefix:
            if i == 0:
                freeq_prefix[ch][i] = 1 if ch == current else 0
            else:
                freeq_prefix[ch][i] = freeq_prefix[ch][i - 1] + (1 if ch == current else 0)

    return freeq_prefix

def query_char_freq(freeq_prefix, ch, i, j):
    if ch not in freeq_prefix:
        return 0
    if i == 0:
        return freeq_prefix[ch][j]
    return freeq_prefix[ch][j] - freeq_prefix[ch][i - 1]


s = "abracadabra"
freeq_prefix = build_char_prefix(s)

print(query_char_freq(freeq_prefix, 'a', 0, 10))  # Output: 5
print(query_char_freq(freeq_prefix, 'b', 1, 4))   # Output: 1
print(query_char_freq(freeq_prefix, 'r', 0, 3))   # Output: 1
print(query_char_freq(freeq_prefix, 'z', 0, 10))  # Output: 0
