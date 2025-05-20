"Step 1: Count frequency of each character"

def first_unique_char(s: str) -> int:
    freq = {}  # create a dictionary to store count
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    "Step 2: Go through the string again and return index of first char with count 1"

    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1

"finnal code"

def first_unique_char(s: str) -> int:
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1


