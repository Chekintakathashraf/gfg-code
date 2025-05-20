def sort_words_by_frequency(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Get unique words preserving original order
    seen = []
    for word in words:
        if word not in seen:
            seen.append(word)

    # Sort seen list by frequency (high to low)
    seen.sort(key=lambda x: (-freq[x], words.index(x)))

    return seen

print(sort_words_by_frequency("apple banana apple orange banana apple"))
# ['apple', 'banana', 'orange']

print(sort_words_by_frequency("dog cat mouse cat dog dog"))
# ['dog', 'cat', 'mouse']

print(sort_words_by_frequency("red blue green blue red"))
# ['red', 'blue', 'green']

