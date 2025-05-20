def most_frequent_word_with_count(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    max_count = 0
    result_word = ""

    for word in words:
        if freq[word] > max_count:
            max_count = freq[word]
            result_word = word

    return (result_word, max_count)


print(most_frequent_word_with_count("this is a test this is only a test"))  # ("this", 2)
print(most_frequent_word_with_count("hello world hello world hello"))       # ("hello", 3)
print(most_frequent_word_with_count("unique only one word"))                # ("unique", 1)

