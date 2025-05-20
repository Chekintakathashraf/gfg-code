def second_most_frequent_word(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Step 1: Find all unique frequency values in descending order
    unique_freqs = sorted(set(freq.values()), reverse=True)

    if len(unique_freqs) < 2:
        return "None"

    second_highest = unique_freqs[1]

    # Step 2: Return the first word with that frequency
    for word in words:
        if freq[word] == second_highest:
            return word

    return "None"

print(second_most_frequent_word("a a b b c c c"))  # "a" or "b"
print(second_most_frequent_word("x y x y x z z z"))  # "y"
print(second_most_frequent_word("apple banana apple orange banana apple"))  # "banana"
print(second_most_frequent_word("unique"))  # "None"
