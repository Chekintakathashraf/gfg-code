def remove_repeated_words(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    result = []
    for word in words:
        if freq[word] == 1:
            result.append(word)

    return result

print(remove_repeated_words("this is a test this is only a test"))  # ['only']
print(remove_repeated_words("apple banana orange apple banana mango"))  # ['orange', 'mango']
print(remove_repeated_words("a b c d e f"))  # ['a', 'b', 'c', 'd', 'e', 'f']
