def sort_by_length_and_frequency(sentence):
    words = sentence.split()
    freq = {}

    # Count frequency of each word
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Preserve first occurrence order
    unique_words = []
    for w in words:
        if w not in unique_words:
            unique_words.append(w)

    # Sort by length ascending, then frequency descending, then original order
    unique_words.sort(key=lambda w: (len(w), -freq[w], words.index(w)))

    return unique_words

print(sort_by_length_and_frequency("apple banana apple orange banana apple"))
# ['apple', 'orange', 'banana']

print(sort_by_length_and_frequency("dog cat mouse cat dog dog"))
# ['cat', 'dog', 'mouse']

print(sort_by_length_and_frequency("red blue green blue red"))
# ['red', 'blue', 'green']


"""Use .sort() with a tuple key for multi-criteria sorting:

    1st: length ascending

    2nd: frequency descending (negative freq)

    3rd: preserve original order by index"""