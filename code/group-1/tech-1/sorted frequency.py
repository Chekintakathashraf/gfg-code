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

#=========================================================================
def second_most_frequent_word_v1(sentence):
    words = sentence.split()
    freq = {}

    # Count frequencies
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Get unique frequencies sorted descending
    unique_freqs = sorted(set(freq.values()), reverse=True)

    if len(unique_freqs) < 2:
        return "None"

    second_highest = unique_freqs[1]

    # Return first word with second highest frequency
    for word in words:
        if freq[word] == second_highest:
            return word

    return "None"

def second_most_frequent_word_v2(sentence):
    words = sentence.split()
    freq = {}

    # Count frequencies
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Get unique frequencies sorted descending
    unique_freqs = sorted(set(freq.values()), reverse=True)

    if len(unique_freqs) < 2:
        return "None"

    second_highest = unique_freqs[1]

    # Sort words by frequency descending, preserve first appearance for tie-break
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    # Sort unique_words by freq descending
    sorted_words = sorted(unique_words, key=lambda w: freq[w], reverse=True)

    # Find first word with second highest frequency in sorted list
    for word in sorted_words:
        if freq[word] == second_highest:
            return word

    return "None"
